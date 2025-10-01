import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.progress_tracker import ProgressTracker
from utils.database import init_database
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Ma'yan English Learning - Tourism & Web Professionals",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
try:
    init_database()
except Exception as e:
    st.error(f"Database initialization error: {str(e)}")

# Initialize session state for user preferences
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Main title
st.title("🌍 Ma'yan English Learning Platform")
st.subheader("For Tourism & Website Professionals - B2 Level")

# Sidebar - User profile
with st.sidebar:
    st.header("👤 User Profile")
    user_name = st.text_input("Your Name", value=st.session_state.user_name, key="user_name_input")
    if user_name != st.session_state.user_name:
        st.session_state.user_name = user_name
        # Reload progress tracker with new user
        st.session_state.progress_tracker = ProgressTracker(user_name)
        st.rerun()

# Initialize progress tracker after user name is set
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker(st.session_state.user_name)

with st.sidebar:
    st.divider()
    st.header("📚 Learning Modules")
    st.write("Navigate using the sidebar pages:")
    st.write("1. 📖 Vocabulary Builder")
    st.write("2. 💬 Conversation Practice")
    st.write("3. ✍️ Grammar Exercises")
    st.write("4. 📰 Reading Comprehension")
    st.write("5. 🗣️ Pronunciation Guide")
    st.write("6. ✉️ Writing Exercises")

# Welcome section
st.markdown("---")
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Welcome to Your English Learning Journey!")
    st.write("""
    This platform is specifically designed for tourism and website professionals in the Ma'yan area.
    Improve your English skills with:
    
    - **Vocabulary**: Learn essential tourism, hospitality, and web industry terms
    - **Conversations**: Practice real workplace scenarios with audio playback
    - **Grammar**: Master professional communication patterns
    - **Reading**: Comprehend industry-specific content
    - **Pronunciation**: Perfect your spoken English with audio guides
    - **Writing**: Develop professional email and customer service skills
    """)

with col2:
    st.info("🎯 **B2 Level Focus**\n\nYou'll learn:\n- Professional communication\n- Customer service excellence\n- Business correspondence\n- Tourism industry terminology")

# Progress Dashboard
st.markdown("---")
st.header("📊 Your Learning Progress")

# Get progress data
progress_data = st.session_state.progress_tracker.get_overall_progress()

# Create metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Words Learned", progress_data['vocabulary']['words_learned'], 
              f"+{progress_data['vocabulary']['words_learned'] - progress_data['vocabulary'].get('last_count', 0)}")

with col2:
    st.metric("Conversations Completed", progress_data['conversations']['completed'], 
              f"{progress_data['conversations']['completion_rate']:.0f}%")

with col3:
    st.metric("Grammar Exercises", progress_data['grammar']['completed'], 
              f"{progress_data['grammar']['accuracy']:.0f}% accuracy")

with col4:
    st.metric("Writing Exercises", progress_data['writing']['completed'], 
              f"{progress_data['writing']['avg_score']:.0f}% avg score")

# Progress visualization
st.subheader("📈 Learning Progress by Module")

col1, col2 = st.columns(2)

with col1:
    # Module completion chart
    module_data = {
        'Module': ['Vocabulary', 'Conversations', 'Grammar', 'Reading', 'Pronunciation', 'Writing'],
        'Completion %': [
            progress_data['vocabulary']['completion_rate'],
            progress_data['conversations']['completion_rate'],
            progress_data['grammar']['completion_rate'],
            progress_data['reading']['completion_rate'],
            progress_data['pronunciation']['completion_rate'],
            progress_data['writing']['completion_rate']
        ]
    }
    
    fig = px.bar(module_data, x='Module', y='Completion %', 
                 title='Module Completion Rates',
                 color='Completion %',
                 color_continuous_scale='Blues')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Learning activity over time
    activity_data = st.session_state.progress_tracker.get_activity_history()
    if activity_data:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=list(range(len(activity_data))),
            y=activity_data,
            mode='lines+markers',
            name='Activities',
            line=dict(color='rgb(49, 130, 189)', width=3)
        ))
        fig.update_layout(
            title='Daily Learning Activity',
            xaxis_title='Days',
            yaxis_title='Activities Completed'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Start learning to see your activity chart!")

# Recent achievements
st.subheader("🏆 Recent Achievements")
achievements = st.session_state.progress_tracker.get_recent_achievements()

if achievements:
    cols = st.columns(min(len(achievements), 3))
    for idx, achievement in enumerate(achievements[:3]):
        with cols[idx]:
            st.success(f"**{achievement['title']}**\n\n{achievement['description']}")
else:
    st.info("Complete exercises to earn achievements!")

# Quick stats
st.markdown("---")
st.subheader("📝 Quick Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Vocabulary Mastery by Category**")
    vocab_stats = progress_data['vocabulary'].get('by_category', {})
    if vocab_stats:
        for category, count in vocab_stats.items():
            st.write(f"• {category}: {count} words")
    else:
        st.write("Start learning vocabulary to see stats!")

with col2:
    st.write("**Grammar Topics Covered**")
    grammar_stats = progress_data['grammar'].get('by_topic', {})
    if grammar_stats:
        for topic, count in grammar_stats.items():
            st.write(f"• {topic}: {count} exercises")
    else:
        st.write("Complete grammar exercises to see stats!")

with col3:
    st.write("**Writing Skills Progress**")
    writing_stats = progress_data['writing'].get('by_type', {})
    if writing_stats:
        for wtype, score in writing_stats.items():
            st.write(f"• {wtype}: {score:.0f}%")
    else:
        st.write("Submit writing exercises to see stats!")

# Tips and recommendations
st.markdown("---")
st.header("💡 Today's Learning Tip")

tips = [
    "Practice pronunciation daily for just 10 minutes to improve your speaking confidence!",
    "Try to use new vocabulary words in real conversations at work today.",
    "Read one tourism article in English every day to improve comprehension.",
    "Write a professional email in English each day to build writing fluency.",
    "Listen to customer service conversations and repeat phrases to improve accent.",
    "Review grammar concepts right before using them in real situations for better retention."
]

import random
st.info(random.choice(tips))

# Footer
st.markdown("---")
st.caption("Ma'yan English Learning Platform - Designed for Tourism & Web Professionals | B2 Level")
