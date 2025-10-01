import streamlit as st
from utils.vocabulary_data import VocabularyData
from utils.audio_utils import AudioUtils
import random

# Initialize
if 'progress_tracker' not in st.session_state:
    from utils.progress_tracker import ProgressTracker
    st.session_state.progress_tracker = ProgressTracker()

if 'vocab_data' not in st.session_state:
    st.session_state.vocab_data = VocabularyData()

if 'current_vocab_index' not in st.session_state:
    st.session_state.current_vocab_index = 0

if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None

# Page header
st.title("📚 Vocabulary Builder")
st.markdown("Master essential tourism and business terminology")

# Category selection
st.subheader("Select a Category")
vocab_data = st.session_state.vocab_data
categories = vocab_data.get_categories()

cols = st.columns(3)
for idx, category in enumerate(categories):
    with cols[idx % 3]:
        if st.button(f"📖 {category['name']}", key=f"cat_{category['name']}", use_container_width=True):
            st.session_state.selected_category = category['name']
            st.session_state.current_vocab_index = 0
            st.session_state.show_answer = False
            st.rerun()

# Display selected category
if st.session_state.selected_category:
    st.markdown("---")
    category_name = st.session_state.selected_category
    st.subheader(f"Category: {category_name}")
    
    # Get words for selected category
    words = vocab_data.get_words_by_category(category_name)
    
    if words:
        # Progress in this category
        progress = st.session_state.progress_tracker.get_vocabulary_progress(category_name)
        learned_words = progress['learned']
        
        st.progress(len(learned_words) / len(words))
        st.caption(f"Progress: {len(learned_words)}/{len(words)} words learned")
        
        # Current word
        current_word = words[st.session_state.current_vocab_index]
        
        # Word display
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"### Word: {current_word['word']}")
            st.markdown(f"**Type:** {current_word['type']}")
            
            # Audio playback
            audio_utils = AudioUtils()
            audio_file = audio_utils.generate_audio(current_word['word'])
            if audio_file:
                st.audio(audio_file, format='audio/mp3')
            
            # Show definition button
            if st.button("Show Definition & Examples", key="show_def"):
                st.session_state.show_answer = True
                st.rerun()
            
            if st.session_state.show_answer:
                st.markdown(f"**Definition:** {current_word['definition']}")
                st.markdown("**Example Sentences:**")
                for example in current_word['examples']:
                    st.markdown(f"- {example}")
                
                # Mark as learned button
                if current_word['word'] not in learned_words:
                    if st.button("✓ Mark as Learned", key="mark_learned"):
                        st.session_state.progress_tracker.add_vocabulary(
                            category_name, 
                            current_word['word']
                        )
                        st.success(f"Great! '{current_word['word']}' marked as learned.")
                        st.rerun()
                else:
                    st.success("✓ Already learned")
        
        with col2:
            # Word count
            st.metric("Current Word", f"{st.session_state.current_vocab_index + 1}/{len(words)}")
            
            # Navigation
            st.markdown("### Navigation")
            
            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("← Previous", disabled=st.session_state.current_vocab_index == 0, use_container_width=True):
                    st.session_state.current_vocab_index -= 1
                    st.session_state.show_answer = False
                    st.rerun()
            
            with col_next:
                if st.button("Next →", disabled=st.session_state.current_vocab_index >= len(words) - 1, use_container_width=True):
                    st.session_state.current_vocab_index += 1
                    st.session_state.show_answer = False
                    st.rerun()
            
            if st.button("Random Word", use_container_width=True):
                st.session_state.current_vocab_index = random.randint(0, len(words) - 1)
                st.session_state.show_answer = False
                st.rerun()
        
        # Quiz mode
        st.markdown("---")
        st.subheader("📝 Quick Quiz")
        
        # Select a random word for quiz
        quiz_word = random.choice(words)
        
        # Create wrong options
        other_words = [w for w in words if w['word'] != quiz_word['word']]
        wrong_options = random.sample(other_words, min(3, len(other_words)))
        
        # Prepare options
        options = [quiz_word['definition']] + [w['definition'] for w in wrong_options]
        random.shuffle(options)
        
        st.markdown(f"**What does '{quiz_word['word']}' mean?**")
        
        answer = st.radio("Choose the correct definition:", options, key=f"quiz_{quiz_word['word']}")
        
        if st.button("Check Answer", key="check_quiz"):
            if answer == quiz_word['definition']:
                st.success("✓ Correct! Well done!")
                st.session_state.progress_tracker.add_vocabulary(category_name, quiz_word['word'])
            else:
                st.error(f"✗ Not quite. The correct answer is: {quiz_word['definition']}")
        
        # Back to category selection
        if st.button("← Back to Categories"):
            st.session_state.selected_category = None
            st.rerun()

else:
    st.info("👆 Select a category above to start learning vocabulary!")
    
    # Show overall progress
    st.markdown("---")
    st.subheader("Your Vocabulary Progress")
    
    for category in categories:
        progress = st.session_state.progress_tracker.get_vocabulary_progress(category['name'])
        words = vocab_data.get_words_by_category(category['name'])
        learned = len(progress['learned'])
        total = len(words)
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{category['name']}**")
            st.progress(learned / total if total > 0 else 0)
        with col2:
            st.metric("Words", f"{learned}/{total}")
