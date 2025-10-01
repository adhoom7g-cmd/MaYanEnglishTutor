import streamlit as st
from utils.writing_data import WritingData

# Initialize
if 'progress_tracker' not in st.session_state:
    from utils.progress_tracker import ProgressTracker
    st.session_state.progress_tracker = ProgressTracker()

if 'writing_data' not in st.session_state:
    st.session_state.writing_data = WritingData()

if 'current_exercise' not in st.session_state:
    st.session_state.current_exercise = None

if 'user_draft' not in st.session_state:
    st.session_state.user_draft = ""

# Page header
st.title("✉️ Writing Exercises")
st.markdown("Craft professional emails and customer responses")

writing_data = st.session_state.writing_data
exercises = writing_data.get_exercises()

# Exercise selection
if st.session_state.current_exercise is None:
    st.subheader("Select a Writing Exercise")
    
    for exercise in exercises:
        with st.expander(f"✍️ {exercise['title']}", expanded=False):
            st.markdown(f"**Type:** {exercise['type']}")
            st.markdown(f"**Scenario:** {exercise['scenario']}")
            st.markdown(f"**Focus:** {', '.join(exercise['focus_skills'])}")
            
            if st.button(f"Start Writing", key=f"start_{exercise['id']}"):
                st.session_state.current_exercise = exercise['id']
                st.session_state.user_draft = ""
                st.rerun()
else:
    # Display current exercise
    exercise = writing_data.get_exercise_by_id(st.session_state.current_exercise)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(f"✍️ {exercise['title']}")
        st.caption(f"{exercise['type']}")
    with col2:
        if st.button("← Back to Exercises"):
            st.session_state.current_exercise = None
            st.rerun()
    
    st.markdown("---")
    
    # Scenario and instructions
    st.markdown("### 📋 Scenario")
    st.info(exercise['scenario'])
    
    st.markdown("### 📝 Your Task")
    st.markdown(exercise['task'])
    
    # Requirements
    if 'requirements' in exercise:
        with st.expander("✓ Requirements Checklist", expanded=True):
            for req in exercise['requirements']:
                st.markdown(f"- {req}")
    
    # Useful phrases
    if 'useful_phrases' in exercise:
        with st.expander("💡 Useful Phrases"):
            for category, phrases in exercise['useful_phrases'].items():
                st.markdown(f"**{category}:**")
                for phrase in phrases:
                    st.markdown(f"- {phrase}")
    
    st.markdown("---")
    
    # Writing area
    st.markdown("### ✍️ Your Response")
    
    # Pre-fill based on type
    template = ""
    if exercise['type'] == 'Email':
        template = f"Subject: \n\nDear [Name],\n\n\n\nBest regards,\n[Your Name]"
    
    user_text = st.text_area(
        "Write your response here:",
        value=st.session_state.user_draft if st.session_state.user_draft else template,
        height=300,
        key="writing_area"
    )
    
    st.session_state.user_draft = user_text
    
    # Word count
    word_count = len(user_text.split())
    col1, col2 = st.columns([3, 1])
    with col2:
        st.metric("Word Count", word_count)
    
    # Submit and get feedback
    if st.button("Get Feedback", type="primary"):
        if len(user_text.strip()) < 20:
            st.warning("Please write a more complete response before getting feedback.")
        else:
            st.session_state.progress_tracker.add_writing_exercise(exercise['id'])
            
            st.markdown("---")
            st.subheader("📊 Feedback")
            
            # Automatic feedback based on requirements
            feedback_points = []
            
            # Check for greeting/closing in emails
            if exercise['type'] == 'Email':
                if 'dear' in user_text.lower() or 'hello' in user_text.lower():
                    feedback_points.append("✓ Good: Appropriate greeting used")
                else:
                    feedback_points.append("✗ Missing: Professional greeting (e.g., 'Dear...', 'Hello...')")
                
                if 'regards' in user_text.lower() or 'sincerely' in user_text.lower() or 'best' in user_text.lower():
                    feedback_points.append("✓ Good: Professional closing used")
                else:
                    feedback_points.append("✗ Missing: Professional closing (e.g., 'Best regards', 'Sincerely')")
                
                if 'subject:' in user_text.lower():
                    feedback_points.append("✓ Good: Subject line included")
                else:
                    feedback_points.append("✗ Missing: Subject line")
            
            # Check for key phrases
            if 'useful_phrases' in exercise:
                found_phrases = 0
                for category, phrases in exercise['useful_phrases'].items():
                    for phrase in phrases:
                        if phrase.lower() in user_text.lower():
                            found_phrases += 1
                            break
                
                if found_phrases >= 2:
                    feedback_points.append(f"✓ Good: Using professional phrases ({found_phrases} found)")
                elif found_phrases == 1:
                    feedback_points.append("⚠ Fair: Consider using more professional phrases from the suggestions")
                else:
                    feedback_points.append("✗ Improvement needed: Use professional phrases from the suggestions")
            
            # Word count feedback
            if exercise['type'] == 'Email' and word_count < 50:
                feedback_points.append("⚠ Your email might be too brief. Add more detail.")
            elif word_count > 200:
                feedback_points.append("⚠ Your response might be too long. Try to be more concise.")
            else:
                feedback_points.append("✓ Good: Appropriate length")
            
            # Display feedback
            for point in feedback_points:
                if point.startswith("✓"):
                    st.success(point)
                elif point.startswith("✗"):
                    st.error(point)
                else:
                    st.warning(point)
            
            # Show model answer
            st.markdown("---")
            st.markdown("### 📄 Model Answer")
            
            with st.expander("View model answer (after you've written your response)", expanded=False):
                st.markdown(exercise['model_answer'])
                
                st.markdown("**Key features of this model answer:**")
                for feature in exercise['key_features']:
                    st.markdown(f"- {feature}")
            
            # Improvement tips
            if 'improvement_tips' in exercise:
                st.markdown("### 💡 Tips for Improvement")
                for tip in exercise['improvement_tips']:
                    st.info(tip)
    
    # Save draft
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Clear Draft"):
            st.session_state.user_draft = ""
            st.rerun()
    
    # Additional exercises
    st.markdown("---")
    st.markdown("### 📚 Related Practice")
    st.markdown(f"**Common mistakes to avoid in {exercise['type'].lower()}s:**")
    
    common_mistakes = {
        'Email': [
            "Using informal language in professional contexts",
            "Forgetting to include subject line",
            "Not proofreading for spelling and grammar",
            "Being too brief or too verbose",
            "Not addressing the recipient properly"
        ],
        'Customer Response': [
            "Sounding defensive or argumentative",
            "Not acknowledging the customer's concern",
            "Forgetting to offer a solution",
            "Using negative language",
            "Not being specific about next steps"
        ]
    }
    
    for mistake in common_mistakes.get(exercise['type'], []):
        st.markdown(f"- {mistake}")
