import streamlit as st
from utils.reading_data import ReadingData

# Initialize
if 'progress_tracker' not in st.session_state:
    from utils.progress_tracker import ProgressTracker
    st.session_state.progress_tracker = ProgressTracker()

if 'reading_data' not in st.session_state:
    st.session_state.reading_data = ReadingData()

if 'current_passage' not in st.session_state:
    st.session_state.current_passage = None

if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# Page header
st.title("📰 Reading Comprehension")
st.markdown("Work with real tourism industry content")

reading_data = st.session_state.reading_data
passages = reading_data.get_passages()

# Passage selection
if st.session_state.current_passage is None:
    st.subheader("Select a Reading Passage")
    
    for passage in passages:
        with st.expander(f"📄 {passage['title']}", expanded=False):
            st.markdown(f"**Type:** {passage['type']}")
            st.markdown(f"**Length:** {passage['word_count']} words")
            st.markdown(f"**Topic:** {passage['topic']}")
            st.markdown(f"**Description:** {passage['description']}")
            
            if st.button(f"Start Reading", key=f"start_{passage['id']}"):
                st.session_state.current_passage = passage['id']
                st.session_state.current_question_index = 0
                st.session_state.user_answers = {}
                st.rerun()
else:
    # Display current passage
    passage = reading_data.get_passage_by_id(st.session_state.current_passage)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(f"📄 {passage['title']}")
        st.caption(f"{passage['type']} | {passage['topic']} | {passage['word_count']} words")
    with col2:
        if st.button("← Back to Passages"):
            st.session_state.current_passage = None
            st.rerun()
    
    st.markdown("---")
    
    # Display the passage
    with st.container():
        st.markdown("### Reading Passage")
        
        # Apply formatting based on type
        if passage['type'] == 'Email':
            st.markdown(f"**From:** {passage.get('from', 'N/A')}")
            st.markdown(f"**To:** {passage.get('to', 'N/A')}")
            st.markdown(f"**Subject:** {passage.get('subject', 'N/A')}")
            st.markdown("---")
        
        # Display text with paragraphs
        for para in passage['text'].split('\n\n'):
            st.markdown(para)
        
        # Vocabulary help
        if 'vocabulary_help' in passage:
            with st.expander("📚 Vocabulary Help"):
                for word, definition in passage['vocabulary_help'].items():
                    st.markdown(f"**{word}:** {definition}")
    
    st.markdown("---")
    
    # Comprehension questions
    st.subheader("Comprehension Questions")
    
    questions = passage['questions']
    
    # Show all questions
    for idx, question in enumerate(questions):
        with st.container():
            st.markdown(f"**Question {idx + 1}:** {question['question']}")
            
            answer_key = f"q_{idx}"
            
            if question['type'] == 'multiple_choice':
                answer = st.radio(
                    "Select your answer:",
                    question['options'],
                    key=answer_key
                )
                
                if st.button("Check", key=f"check_{idx}"):
                    if answer == question['correct']:
                        st.success("✓ Correct!")
                        st.session_state.user_answers[idx] = True
                        st.session_state.progress_tracker.add_reading_exercise(passage['id'])
                    else:
                        st.error(f"✗ Incorrect. The correct answer is: {question['correct']}")
                        st.session_state.user_answers[idx] = False
                    
                    if 'explanation' in question:
                        st.info(f"💡 {question['explanation']}")
            
            elif question['type'] == 'short_answer':
                answer = st.text_area("Your answer:", key=answer_key, height=100)
                
                if st.button("Check", key=f"check_{idx}"):
                    st.info(f"**Model answer:** {question['model_answer']}")
                    
                    if 'key_points' in question:
                        st.markdown("**Your answer should include:**")
                        for point in question['key_points']:
                            st.markdown(f"- {point}")
                    
                    # Self-assessment
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("My answer covers the key points", key=f"self_correct_{idx}"):
                            st.session_state.user_answers[idx] = True
                            st.session_state.progress_tracker.add_reading_exercise(passage['id'])
                            st.success("Well done!")
                    with col2:
                        if st.button("I need to review", key=f"self_review_{idx}"):
                            st.session_state.user_answers[idx] = False
                            st.info("Read the passage again and look for the key information!")
            
            elif question['type'] == 'true_false':
                answer = st.radio(
                    "True or False?",
                    ["True", "False"],
                    key=answer_key
                )
                
                if st.button("Check", key=f"check_{idx}"):
                    if answer == question['correct']:
                        st.success("✓ Correct!")
                        st.session_state.user_answers[idx] = True
                        st.session_state.progress_tracker.add_reading_exercise(passage['id'])
                    else:
                        st.error(f"✗ Incorrect. The correct answer is: {question['correct']}")
                        st.session_state.user_answers[idx] = False
                    
                    if 'explanation' in question:
                        st.info(f"💡 {question['explanation']}")
            
            st.markdown("---")
    
    # Summary
    if st.session_state.user_answers:
        st.subheader("📊 Your Results")
        
        correct = sum(1 for v in st.session_state.user_answers.values() if v)
        total = len(st.session_state.user_answers)
        
        st.progress(correct / total if total > 0 else 0)
        st.markdown(f"**Score:** {correct}/{total} ({(correct/total*100) if total > 0 else 0:.1f}%)")
        
        if correct == total:
            st.balloons()
            st.success("🎉 Perfect score! Excellent comprehension!")
        elif correct >= total * 0.7:
            st.success("👏 Good job! You understood the main points.")
        else:
            st.info("📚 Try reading the passage again and pay attention to the details.")
    
    # Discussion questions
    if 'discussion_questions' in passage:
        st.markdown("---")
        st.subheader("💭 Discussion & Reflection")
        
        for dq in passage['discussion_questions']:
            with st.expander(dq):
                reflection = st.text_area("Your thoughts:", key=f"discuss_{dq}", height=100)
                if reflection:
                    st.info("Great reflection! These questions help you think more deeply about the content.")
