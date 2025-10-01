
import streamlit as st
from utils.progress_tracker import ProgressTracker

# Initialize progress tracker
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

# Page header
st.title("📘 Daily English Lessons")
st.subheader("Daily English Lessons for Tourism & Web/Tech")

st.write("Welcome! This section provides *English vocabulary, sentences, and exercises* with a focus on tourism and technology.")

# Lesson 1 Content
st.header("✨ Lesson 1: Travel & Business Events")

st.markdown("#### 🗒 Vocabulary (20 words)")

# Vocabulary with pronunciation and examples
vocabulary_data = [
    ("Destination", "وجهة", "/ˌdestɪˈneɪʃən/", "Egypt is a popular tourist destination."),
    ("Success", "نجاح", "/səkˈses/", "The event was a great success."),
    ("Supplier", "مورّد", "/səˈplaɪər/", "We work with reliable suppliers."),
    ("Vendor", "بائع / مزوّد", "/ˈvendər/", "The vendor provided excellent service."),
    ("Trade show", "معرض تجاري", "/treɪd ʃoʊ/", "We attended the annual trade show."),
    ("Relationship", "علاقة", "/rɪˈleɪʃənʃɪp/", "Building good relationships is important."),
    ("Client", "عميل", "/ˈklaɪənt/", "Our client was very satisfied."),
    ("Confidence", "ثقة", "/ˈkɒnfɪdəns/", "She spoke with confidence."),
    ("Investment", "استثمار", "/ɪnˈvestmənt/", "This is a good investment opportunity."),
    ("Growth", "نمو", "/ɡroʊθ/", "The company showed steady growth."),
    ("Opportunity", "فرصة", "/ˌɒpərˈtuːnəti/", "This is a great opportunity to learn."),
    ("Energized", "مليء بالطاقة", "/ˈenərˌdʒaɪzd/", "The team felt energized after the meeting."),
    ("Welcoming", "ترحيبي", "/ˈwelkəmɪŋ/", "The staff were very welcoming."),
    ("Family-oriented", "يهتم بالعائلة", "/ˈfæməli ˈɔːriˌentɪd/", "This is a family-oriented resort."),
    ("Knowledge", "معرفة", "/ˈnɒlɪdʒ/", "He has extensive knowledge of tourism."),
    ("Session", "جلسة", "/ˈseʃən/", "The training session was informative."),
    ("Speaker", "متحدث", "/ˈspiːkər/", "The guest speaker was excellent."),
    ("Respect", "احترام", "/rɪˈspekt/", "We treat all guests with respect."),
    ("Experience", "تجربة", "/ɪkˈspɪriəns/", "This was an unforgettable experience."),
    ("Annual", "سنوي", "/ˈænjuəl/", "We hold an annual conference."),
]

# Display vocabulary in an interactive format
for i, (word, arabic, phonetic, example) in enumerate(vocabulary_data):
    with st.expander(f"{i+1}. **{word}** – {arabic}"):
        st.write(f"**Pronunciation:** {phonetic}")
        st.write(f"**Example:** {example}")
        
        # Add to learned vocabulary when expanded
        if st.button(f"Mark as learned", key=f"learn_{word}"):
            st.session_state.progress_tracker.add_vocabulary_word(word, "Business & Events")
            st.success(f"Added '{word}' to your learned vocabulary!")

st.markdown("#### 📝 Example Sentences")

sentences = [
    "This event was the best experience I have had in years.",
    "We built strong relationships with many suppliers.",
    "I have the confidence to sell travel packages now.",
    "The company made a big investment in this event.",
    "Meeting new clients is always an opportunity.",
    "The trade show was full of useful information.",
    "Every session had a great speaker.",
    "The staff were very welcoming and friendly.",
    "This will become an annual event.",
    "Respect is important for business growth."
]

for i, sentence in enumerate(sentences, 1):
    st.write(f"{i}. {sentence}")

# Interactive exercise section
st.markdown("#### 🏠 Practice Exercises")

st.write("**Exercise 1:** Write 5 new sentences using these words:")
target_words = ["supplier", "client", "growth", "confidence", "respect"]

for word in target_words:
    user_sentence = st.text_area(f"Write a sentence using '{word}':", key=f"sentence_{word}", height=60)
    if user_sentence and len(user_sentence.strip()) > 10:
        if word.lower() in user_sentence.lower():
            st.success(f"✅ Great! You used '{word}' correctly.")
        else:
            st.warning(f"⚠️ Make sure to include the word '{word}' in your sentence.")

st.write("**Exercise 2:** Read the 10 sentences aloud twice.")
st.info("💡 Tip: Click on each sentence and practice pronunciation. Focus on stress and intonation.")

st.write("**Exercise 3:** Write a personal sentence using 'annual':")
annual_sentence = st.text_area("Your sentence with 'annual':", height=60)

if annual_sentence and "annual" in annual_sentence.lower():
    st.success("✅ Excellent! You've completed the exercise.")
    if st.button("Submit Lesson Progress"):
        # Track lesson completion
        st.session_state.progress_tracker.complete_lesson("Lesson 1: Travel & Business Events")
        st.balloons()
        st.success("🎉 Lesson 1 completed! Great job!")

# Progress tracking
st.markdown("---")
st.subheader("📊 Your Progress")

progress = st.session_state.progress_tracker.get_lesson_progress()
if progress:
    st.write(f"**Lessons Completed:** {len(progress)}")
    for lesson in progress:
        st.write(f"✅ {lesson}")
else:
    st.write("Complete your first lesson to see progress!")

# Navigation tips
st.markdown("---")
st.info("💡 **Next Steps:** Visit other pages to practice pronunciation, grammar, and conversation skills with the vocabulary you've learned!")
