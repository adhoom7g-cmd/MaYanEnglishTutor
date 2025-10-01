import streamlit as st
from utils.conversation_data import ConversationData
from utils.audio_utils import AudioUtils

# Initialize
if 'progress_tracker' not in st.session_state:
    from utils.progress_tracker import ProgressTracker
    st.session_state.progress_tracker = ProgressTracker()

if 'conversation_data' not in st.session_state:
    st.session_state.conversation_data = ConversationData()

if 'current_scenario' not in st.session_state:
    st.session_state.current_scenario = None

if 'current_line_index' not in st.session_state:
    st.session_state.current_line_index = 0

# Page header
st.title("💬 Conversation Practice")
st.markdown("Practice real-world workplace scenarios with audio playback")

# Scenario selection
conversation_data = st.session_state.conversation_data
scenarios = conversation_data.get_scenarios()

if st.session_state.current_scenario is None:
    st.subheader("Select a Scenario")
    
    for scenario in scenarios:
        with st.expander(f"🎭 {scenario['title']}", expanded=False):
            st.markdown(f"**Context:** {scenario['context']}")
            st.markdown(f"**Difficulty:** {scenario['difficulty']}")
            st.markdown(f"**Focus Skills:** {', '.join(scenario['skills'])}")
            
            if st.button(f"Start Practice", key=f"start_{scenario['id']}"):
                st.session_state.current_scenario = scenario['id']
                st.session_state.current_line_index = 0
                st.rerun()
else:
    # Display current scenario
    scenario = conversation_data.get_scenario_by_id(st.session_state.current_scenario)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(f"🎭 {scenario['title']}")
        st.markdown(f"**Context:** {scenario['context']}")
    with col2:
        if st.button("← Back to Scenarios"):
            st.session_state.current_scenario = None
            st.rerun()
    
    st.markdown("---")
    
    # Conversation display
    conversation = scenario['conversation']
    audio_utils = AudioUtils()
    
    # Show conversation up to current line
    for idx, line in enumerate(conversation[:st.session_state.current_line_index + 1]):
        speaker_emoji = "👤" if line['speaker'] == "Staff" or line['speaker'] == "Employee" or line['speaker'] == "You" else "👥"
        
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**{speaker_emoji} {line['speaker']}:**")
                st.markdown(f"_{line['text']}_")
                
                if 'translation' in line:
                    with st.expander("See helpful notes"):
                        st.markdown(f"**Key phrases:** {line['translation']}")
            
            with col2:
                # Audio playback for this line
                audio_file = audio_utils.generate_audio(line['text'])
                if audio_file:
                    st.audio(audio_file, format='audio/mp3')
        
        st.markdown("")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← Previous", disabled=st.session_state.current_line_index == 0, use_container_width=True):
            st.session_state.current_line_index -= 1
            st.rerun()
    
    with col2:
        st.metric("Progress", f"{st.session_state.current_line_index + 1}/{len(conversation)}")
    
    with col3:
        if st.session_state.current_line_index < len(conversation) - 1:
            if st.button("Next →", use_container_width=True):
                st.session_state.current_line_index += 1
                st.rerun()
        else:
            if st.button("✓ Complete", use_container_width=True):
                st.session_state.progress_tracker.add_conversation(scenario['id'])
                st.success("Conversation completed! Great job!")
                st.balloons()
    
    # Play entire conversation
    st.markdown("---")
    if st.button("🔊 Play Entire Conversation"):
        st.info("Playing full conversation...")
        for line in conversation:
            st.markdown(f"**{line['speaker']}:** {line['text']}")
    
    # Practice section
    st.markdown("---")
    st.subheader("🎯 Your Turn to Practice")
    
    st.markdown("Record yourself or practice speaking the following lines:")
    
    # Show staff/employee lines for practice
    practice_lines = [line for line in conversation if line['speaker'] in ['Staff', 'Employee', 'You']]
    
    for idx, line in enumerate(practice_lines):
        with st.expander(f"Practice line {idx + 1}"):
            st.markdown(f"**Say:** _{line['text']}_")
            
            # Audio playback
            audio_file = audio_utils.generate_audio(line['text'])
            if audio_file:
                st.audio(audio_file, format='audio/mp3')
            
            if 'translation' in line:
                st.markdown(f"**Tips:** {line['translation']}")
    
    # Key phrases section
    st.markdown("---")
    st.subheader("📌 Key Phrases from This Scenario")
    
    if 'key_phrases' in scenario:
        for phrase in scenario['key_phrases']:
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"- **{phrase['phrase']}**")
                st.caption(phrase['usage'])
            with col2:
                audio_file = audio_utils.generate_audio(phrase['phrase'])
                if audio_file:
                    st.audio(audio_file, format='audio/mp3')
