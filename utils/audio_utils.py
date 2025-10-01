"""Audio generation utilities using Google Text-to-Speech"""

import streamlit as st
from gtts import gTTS
from io import BytesIO
import hashlib

class AudioUtils:
    """Utility class for generating audio from text using gTTS"""
    
    def __init__(self, language='en', tld='com'):
        """
        Initialize AudioUtils
        
        Args:
            language: Language code (default: 'en' for English)
            tld: Top-level domain for accent (default: 'com' for US English)
                 Options: 'com' (US), 'co.uk' (UK), 'com.au' (Australia), etc.
        """
        self.language = language
        self.tld = tld
        self.cache = {}
    
    def generate_audio(self, text, slow=False):
        """
        Generate audio from text using gTTS
        
        Args:
            text: Text to convert to speech
            slow: Whether to speak slowly (default: False)
        
        Returns:
            BytesIO object containing MP3 audio data, or None if generation fails
        """
        if not text or not text.strip():
            return None
        
        # Create cache key
        cache_key = self._create_cache_key(text, slow)
        
        # Check cache
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            # Generate speech
            tts = gTTS(text=text, lang=self.language, slow=slow, tld=self.tld)
            
            # Save to BytesIO object
            audio_bytes = BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            
            # Cache the result
            self.cache[cache_key] = audio_bytes
            
            return audio_bytes
            
        except Exception as e:
            st.error(f"Error generating audio: {str(e)}")
            return None
    
    def play_text(self, text, slow=False, key=None):
        """
        Generate and display audio player for text
        
        Args:
            text: Text to convert to speech
            slow: Whether to speak slowly
            key: Unique key for Streamlit audio widget
        """
        audio_data = self.generate_audio(text, slow)
        
        if audio_data:
            # Create a new BytesIO object for playback (to avoid seek issues)
            playback_data = BytesIO(audio_data.getvalue())
            st.audio(playback_data, format='audio/mp3', start_time=0)
        else:
            st.warning("Unable to generate audio for this text.")
    
    def get_audio_html(self, text, slow=False):
        """
        Generate HTML audio player (for advanced use cases)
        
        Args:
            text: Text to convert to speech
            slow: Whether to speak slowly
        
        Returns:
            HTML string with embedded audio player
        """
        import base64
        
        audio_data = self.generate_audio(text, slow)
        
        if audio_data:
            # Encode to base64
            audio_base64 = base64.b64encode(audio_data.getvalue()).decode()
            
            # Create HTML audio element
            html = f'''
            <audio controls style="width: 100%;">
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
            '''
            return html
        
        return None
    
    def play_comparison(self, text, label_normal="Normal Speed", label_slow="Slow Speed"):
        """
        Display side-by-side audio players for normal and slow speech
        
        Args:
            text: Text to convert to speech
            label_normal: Label for normal speed player
            label_slow: Label for slow speed player
        """
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**{label_normal}**")
            self.play_text(text, slow=False, key=f"normal_{hash(text)}")
        
        with col2:
            st.write(f"**{label_slow}**")
            self.play_text(text, slow=True, key=f"slow_{hash(text)}")
    
    def clear_cache(self):
        """Clear the audio cache"""
        self.cache = {}
        st.success("Audio cache cleared!")
    
    def _create_cache_key(self, text, slow):
        """Create a unique cache key for text and speed combination"""
        key_string = f"{text}_{slow}_{self.language}_{self.tld}"
        return hashlib.md5(key_string.encode()).hexdigest()
    
    @staticmethod
    def get_phonetic_breakdown(text):
        """
        Get simple phonetic breakdown hints (for display purposes)
        This is a simple helper - actual phonetic data should come from the data files
        
        Args:
            text: Text to analyze
        
        Returns:
            Dictionary with syllable information
        """
        # This is a simplified version - actual phonetic data comes from pronunciation_data
        words = text.split()
        return {
            'word_count': len(words),
            'estimated_syllables': sum(AudioUtils._count_syllables(word) for word in words),
            'words': words
        }
    
    @staticmethod
    def _count_syllables(word):
        """Simple syllable counter (rough approximation)"""
        word = word.lower()
        vowels = 'aeiouy'
        syllable_count = 0
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel
        
        # Adjust for silent 'e'
        if word.endswith('e'):
            syllable_count -= 1
        
        # Ensure at least 1 syllable
        if syllable_count == 0:
            syllable_count = 1
        
        return syllable_count
