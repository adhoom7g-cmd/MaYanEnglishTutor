import streamlit as st
from gtts import gTTS
import base64
import os
import tempfile
from io import BytesIO

class AudioHelper:
    """Helper class for generating and playing audio content"""
    
    def __init__(self, language='en', slow=False):
        self.language = language
        self.slow = slow
        self.audio_cache = {}
    
    def text_to_speech(self, text, slow=None):
        """
        Convert text to speech and return audio player HTML
        
        Args:
            text: Text to convert to speech
            slow: Whether to speak slowly (overrides instance setting if provided)
        
        Returns:
            HTML audio player string
        """
        try:
            # Use instance slow setting if not specified
            is_slow = slow if slow is not None else self.slow
            
            # Check cache
            cache_key = f"{text}_{is_slow}"
            if cache_key in self.audio_cache:
                return self.audio_cache[cache_key]
            
            # Generate speech
            tts = gTTS(text=text, lang=self.language, slow=is_slow)
            
            # Save to BytesIO object
            audio_bytes = BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            
            # Encode to base64
            audio_base64 = base64.b64encode(audio_bytes.read()).decode()
            
            # Create HTML audio player
            audio_html = f'''
                <audio controls style="width: 100%;">
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                    Your browser does not support the audio element.
                </audio>
            '''
            
            # Cache the result
            self.audio_cache[cache_key] = audio_html
            
            return audio_html
            
        except Exception as e:
            st.error(f"Error generating audio: {str(e)}")
            return None
    
    def play_audio(self, text, slow=None, label="🔊 Listen"):
        """
        Generate and display audio player with a label
        
        Args:
            text: Text to convert to speech
            slow: Whether to speak slowly
            label: Label to display above audio player
        """
        st.write(label)
        audio_html = self.text_to_speech(text, slow)
        if audio_html:
            st.markdown(audio_html, unsafe_allow_html=True)
    
    def play_audio_comparison(self, text, label_normal="Normal Speed", label_slow="Slow Speed"):
        """
        Display both normal and slow speed audio players for comparison
        
        Args:
            text: Text to convert to speech
            label_normal: Label for normal speed audio
            label_slow: Label for slow speed audio
        """
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(label_normal)
            audio_html_normal = self.text_to_speech(text, slow=False)
            if audio_html_normal:
                st.markdown(audio_html_normal, unsafe_allow_html=True)
        
        with col2:
            st.write(label_slow)
            audio_html_slow = self.text_to_speech(text, slow=True)
            if audio_html_slow:
                st.markdown(audio_html_slow, unsafe_allow_html=True)
    
    def clear_cache(self):
        """Clear the audio cache"""
        self.audio_cache = {}
    
    @staticmethod
    def create_pronunciation_guide(word, phonetic, example_sentence):
        """
        Create a pronunciation guide with word, phonetic spelling, and example
        
        Args:
            word: The word to practice
            phonetic: Phonetic spelling
            example_sentence: Example sentence using the word
        
        Returns:
            Dictionary with formatted pronunciation guide
        """
        return {
            'word': word,
            'phonetic': phonetic,
            'example': example_sentence
        }
