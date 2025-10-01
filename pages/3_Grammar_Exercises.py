import streamlit as st
from utils.grammar_data import GrammarData
import random

# Initialize
if 'progress_tracker' not in st.session_state:
    from utils.progress_tracker import ProgressTracker
    st.session_state.progress_tracker = ProgressTracker()

if 'grammar_data' not in st.session_state:
    st.session_state.grammar_data = GrammarData()

if 'current_topic' not in st.session_state:
    st.session_state.current_topic = None

if 'current_exercise_index' not in st.session_state:
    st.session_state.current_exercise_index = 0

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# Page header
st.title("✍️ Grammar Exercises")
st.markdown("Master business communication grammar")

grammar_data = st.session_state.grammar_data
topics = grammar_data.get_topics()

# Topic selection
if st.session_state.current_topic is None:
    st.subheader("Select a Grammar Topic")
    
    for topic in topics:
        with st.expander(f"📖 {topic['title']}", expanded=False):
            st.markdown(f"**Focus:** {topic['description']}")
            st.markdown(f"**Difficulty:** {topic['difficulty']}")
            st.markdown(f"**Exercises:** {topic['exercise_count']}")
            
            if st.button(f"Start Exercises", key=f"start_{topic['id']}"):
                st.session_state.current_topic = topic['id']
                st.session_state.current_exercise_index = 0
                st.session_state.user_answers = {}
                st.rerun()
else:
    # Display current topic
    topic = grammar_data.get_topic_by_id(st.session_state.current_topic)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(f"📖 {topic['title']}")
        st.markdown(f"**Focus:** {topic['description']}")
    with col2:
        if st.button("← Back to Topics"):
            st.session_state.current_topic = None
            st.rerun()
    
    # Grammar explanation
    with st.expander("📚 Grammar Rules & Examples", expanded=True):
        st.markdown(topic['explanation'])
        
        if topic.get('examples'):
            st.markdown("**Examples:**")
            for example in topic['examples']:
                st.markdown(f"✓ {example}")
    
    st.markdown("---")
    
    # Exercises
    exercises = topic['exercises']
    current_ex_idx = st.session_state.current_exercise_index
    
    if current_ex_idx < len(exercises):
        current_exercise = exercises[current_ex_idx]
        
        st.subheader(f"Exercise {current_ex_idx + 1} of {len(exercises)}")
        
        # Different exercise types
        if current_exercise['type'] == 'multiple_choice':
            st.markdown(f"**Question:** {current_exercise['question']}")
            
            answer_key = f"ex_{current_ex_idx}"
            
            answer = st.radio(
                "Choose the correct answer:",
                current_exercise['options'],
                key=answer_key
            )
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("Check Answer", key=f"check_{current_ex_idx}"):
                    if answer == current_exercise['correct']:
                        st.success("✓ Correct!")
                        st.session_state.user_answers[current_ex_idx] = True
                        st.session_state.progress_tracker.add_grammar_exercise(topic['id'])
                    else:
                        st.error(f"✗ Incorrect. The correct answer is: {current_exercise['correct']}")
                        st.session_state.user_answers[current_ex_idx] = False
                    
                    if 'explanation' in current_exercise:
                        st.info(f"💡 {current_exercise['explanation']}")
        
        elif current_exercise['type'] == 'fill_blank':
            st.markdown(f"**Complete the sentence:**")
            st.markdown(current_exercise['sentence'])
            
            answer_key = f"ex_{current_ex_idx}"
            user_answer = st.text_input("Your answer:", key=answer_key)
            
            if st.button("Check Answer", key=f"check_{current_ex_idx}"):
                # Check if answer matches any acceptable answers
                correct_answers = current_exercise['correct'] if isinstance(current_exercise['correct'], list) else [current_exercise['correct']]
                
                if user_answer.strip().lower() in [ans.lower() for ans in correct_answers]:
                    st.success("✓ Correct!")
                    st.session_state.user_answers[current_ex_idx] = True
                    st.session_state.progress_tracker.add_grammar_exercise(topic['id'])
                else:
                    st.error(f"✗ Incorrect. Correct answer(s): {', '.join(correct_answers)}")
                    st.session_state.user_answers[current_ex_idx] = False
                
                if 'explanation' in current_exercise:
                    st.info(f"💡 {current_exercise['explanation']}")
        
        elif current_exercise['type'] == 'rewrite':
            st.markdown(f"**Rewrite the following sentence:**")
            st.markdown(f"_{current_exercise['sentence']}_")
            st.markdown(f"**Task:** {current_exercise['instruction']}")
            
            answer_key = f"ex_{current_ex_idx}"
            user_answer = st.text_area("Your rewritten sentence:", key=answer_key, height=100)
            
            if st.button("Check Answer", key=f"check_{current_ex_idx}"):
                st.info(f"**Model answer:** {current_exercise['model_answer']}")
                st.markdown("**Compare your answer with the model answer above.**")
                
                if 'explanation' in current_exercise:
                    st.info(f"💡 {current_exercise['explanation']}")
                
                # Let user self-assess
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("My answer is correct", key=f"self_correct_{current_ex_idx}"):
                        st.session_state.user_answers[current_ex_idx] = True
                        st.session_state.progress_tracker.add_grammar_exercise(topic['id'])
                        st.success("Great job!")
                with col2:
                    if st.button("I need to review", key=f"self_review_{current_ex_idx}"):
                        st.session_state.user_answers[current_ex_idx] = False
                        st.info("Review the grammar rules and try again!")
        
        # Navigation
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("← Previous", disabled=current_ex_idx == 0, use_container_width=True):
                st.session_state.current_exercise_index -= 1
                st.rerun()
        
        with col2:
            # Progress
            correct_count = sum(1 for v in st.session_state.user_answers.values() if v)
            st.metric("Your Score", f"{correct_count}/{len(st.session_state.user_answers)}")
        
        with col3:
            if current_ex_idx < len(exercises) - 1:
                if st.button("Next →", use_container_width=True):
                    st.session_state.current_exercise_index += 1
                    st.rerun()
            else:
                if st.button("✓ Finish", use_container_width=True):
                    correct = sum(1 for v in st.session_state.user_answers.values() if v)
                    total = len(st.session_state.user_answers)
                    
                    st.success(f"Topic completed! Your score: {correct}/{total}")
                    
                    if correct == total:
                        st.balloons()
                        st.markdown("🎉 Perfect score! Excellent work!")
                    elif correct >= total * 0.7:
                        st.markdown("👏 Good job! Consider reviewing the questions you missed.")
                    else:
                        st.markdown("📚 Keep practicing! Review the grammar rules and try again.")
    
    # Summary section
    if st.session_state.user_answers:
        st.markdown("---")
        st.subheader("📊 Exercise Summary")
        
        correct = sum(1 for v in st.session_state.user_answers.values() if v)
        total = len(st.session_state.user_answers)
        
        st.progress(correct / total if total > 0 else 0)
        st.markdown(f"**Correct answers:** {correct}/{total} ({(correct/total*100) if total > 0 else 0:.1f}%)")
