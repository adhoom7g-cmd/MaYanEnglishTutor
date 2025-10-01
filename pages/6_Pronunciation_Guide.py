import streamlit as st
from utils.pronunciation_data import PronunciationData
from utils.audio_utils import AudioUtils

# Initialize
if 'pronunciation_data' not in st.session_state:
    st.session_state.pronunciation_data = PronunciationData()

if 'current_category' not in st.session_state:
    st.session_state.current_category = None

# Page header
st.title("🎤 Pronunciation Guide")
st.markdown("Perfect your speaking with audio examples")

pronunciation_data = st.session_state.pronunciation_data
categories = pronunciation_data.get_categories()
audio_utils = AudioUtils()

# Category selection
if st.session_state.current_category is None:
    st.subheader("Select a Category")
    
    cols = st.columns(2)
    for idx, category in enumerate(categories):
        with cols[idx % 2]:
            if st.button(f"🔊 {category['name']}", key=f"cat_{category['id']}", use_container_width=True):
                st.session_state.current_category = category['id']
                st.rerun()
else:
    # Display current category
    category = pronunciation_data.get_category_by_id(st.session_state.current_category)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(f"🔊 {category['name']}")
        st.markdown(f"_{category['description']}_")
    with col2:
        if st.button("← Back"):
            st.session_state.current_category = None
            st.rerun()
    
    st.markdown("---")
    
    # Pronunciation tips
    if 'tips' in category:
        with st.expander("💡 Pronunciation Tips", expanded=True):
            for tip in category['tips']:
                st.markdown(f"- {tip}")
    
    st.markdown("---")
    
    # Display phrases
    st.subheader("Practice Phrases")
    
    phrases = category['phrases']
    
    for idx, phrase_data in enumerate(phrases):
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {phrase_data['phrase']}")
                
                if 'phonetic' in phrase_data:
                    st.caption(f"Phonetic: /{phrase_data['phonetic']}/")
                
                st.markdown(f"**Usage:** {phrase_data['usage']}")
                
                if 'stress_pattern' in phrase_data:
                    st.markdown(f"**Stress:** {phrase_data['stress_pattern']}")
                
                # Example sentences
                if 'examples' in phrase_data:
                    with st.expander("See example sentences"):
                        for example in phrase_data['examples']:
                            st.markdown(f"- {example}")
            
            with col2:
                # Audio playback
                audio_file = audio_utils.generate_audio(phrase_data['phrase'])
                if audio_file:
                    st.audio(audio_file, format='audio/mp3')
                
                # Slow version
                if st.button("🐢 Slow", key=f"slow_{idx}"):
                    slow_audio = audio_utils.generate_audio(phrase_data['phrase'], slow=True)
                    if slow_audio:
                        st.audio(slow_audio, format='audio/mp3')
            
            st.markdown("---")
    
    # Common pronunciation challenges
    if 'challenges' in category:
        st.markdown("---")
        st.subheader("⚠️ Common Pronunciation Challenges")
        
        for challenge in category['challenges']:
            with st.expander(challenge['issue']):
                st.markdown(f"**Problem:** {challenge['problem']}")
                st.markdown(f"**Solution:** {challenge['solution']}")
                
                if 'practice_words' in challenge:
                    st.markdown("**Practice words:**")
                    
                    cols = st.columns(3)
                    for idx, word in enumerate(challenge['practice_words']):
                        with cols[idx % 3]:
                            st.markdown(f"**{word}**")
                            audio_file = audio_utils.generate_audio(word)
                            if audio_file:
                                st.audio(audio_file, format='audio/mp3')
    
    # Minimal pairs (for sound discrimination)
    if 'minimal_pairs' in category:
        st.markdown("---")
        st.subheader("🔄 Minimal Pairs Practice")
        st.caption("Listen carefully to the difference between these similar-sounding words")
        
        for pair in category['minimal_pairs']:
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.markdown(f"**{pair['word1']}**")
                audio1 = audio_utils.generate_audio(pair['word1'])
                if audio1:
                    st.audio(audio1, format='audio/mp3')
            
            with col2:
                st.markdown(f"**{pair['word2']}**")
                audio2 = audio_utils.generate_audio(pair['word2'])
                if audio2:
                    st.audio(audio2, format='audio/mp3')
            
            with col3:
                st.caption(pair['difference'])
            
            st.markdown("---")

# Overall pronunciation resources
st.markdown("---")
st.subheader("📚 Additional Resources")

st.markdown("""
**General Pronunciation Tips:**
- Practice daily for at least 10-15 minutes
- Record yourself and compare with native speakers
- Pay attention to word stress and intonation
- Practice difficult sounds in isolation first, then in words, then in sentences
- Don't worry about having a perfect accent - clarity is more important
- Listen to English podcasts and videos regularly

**Key Areas to Focus On:**
1. **Word Stress**: English words have stressed syllables - getting this wrong can make words hard to understand
2. **Sentence Intonation**: Rising intonation for questions, falling for statements
3. **Connected Speech**: Words flow together in natural speech
4. **Consonant Clusters**: Practice words with multiple consonants together (e.g., "strengths")
5. **Vowel Sounds**: English has# thoughts

I need to create a comprehensive Streamlit-based English learning application for tourism and website professionals in the Ma'yan area, focusing on B2-level speaking and practical communication. The application should include:

1. Interactive vocabulary builder with tourism/business categories
2. Conversation practice scenarios with audio playback
3. Grammar exercises for business communication
4. Reading comprehension tasks
5. Progress tracking dashboard with visualizations
6. Pronunciation guide with audio
7. Writing exercises with feedback

I'll structure this as a multi-page Streamlit application with:
- Main dashboard showing progress
- Vocabulary builder module
- Conversation practice module
- Grammar exercises module
- Reading comprehension module
- Pronunciation guide module
- Writing exercises module

I'll use gTTS for text-to-speech, Pandas for data management, and Plotly for visualizations. All progress will be tracked using Streamlit session state and can be persisted to JSON files.

The application will bind to port 5000 on 0.0.0.0 as specified in the configuration.

# useful_guidelines_from_blueprints

- Add server configuration to `.streamlit/config.toml` with headless=true, address="0.0.0.0", port=5000
- Use `st.rerun()` instead of `experimental_rerun`
- Maintain default font settings unless specifically requested
- Focus on content organization and interactive elements
- Use standard Streamlit functions for application flow control

# directory_structure

```json
[
    {"path": ".streamlit/config.toml", "status": "new"},
    {"path": "app.py", "status": "new"},
    {"path": "pages/1_vocabulary_builder.py", "status": "new"},
    {"path": "pages/2_conversation_practice.py", "status": "new"},
    {"path": "pages/3_grammar_exercises.py", "status": "new"},
    {"path": "pages/4_reading_comprehension.py", "status": "new"},
    {"path": "pages/5_pronunciation_guide.py", "status": "new"},
    {"path": "pages/6_writing_exercises.py", "status": "new"},
    {"path": "utils/audio_helper.py", "status": "new"},
    {"path": "utils/progress_tracker.py", "status": "new"},
    {"path": "data/vocabulary_data.py", "status": "new"},
    {"path": "data/conversation_scenarios.py", "status": "new"},
    {"path": "data/grammar_exercises.py", "status": "new"},
    {"path": "data/reading_content.py", "status": "new"},
    {"path": "data/pronunciation_phrases.py", "status": "new"},
    {"path": "data/writing_prompts.py", "status": "new"}
]
