import streamlit as st
from textblob import TextBlob
import textwrap
import nltk

# Download required NLTK data
nltk.download('punkt')

# Streamlit UI setup
st.set_page_config(page_title="Emotion & Sentiment Analyzer")
st.title("Emotion & Sentiment Analyzer")
st.markdown("Analyze emotions in social media text using sentiment analysis.")

# Text input area
text = st.text_area("Enter or paste conversation here:")

# Button to analyze sentiment
if st.button("Analyze"):
    if text:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Simple emotion mapping
        if polarity > 0.1:
            sentiment = "Positive"
            emotion = "Happy / Excited"
        elif polarity < -0.1:
            sentiment = "Negative"
            emotion = "Angry / Sad"
        else:
            sentiment = "Neutral"
            emotion = "Calm / Uncertain"

        # Display results
        st.subheader("Analysis Result")
        st.markdown(f"**Text:** {textwrap.fill(text, width=100)}")
        st.markdown(f"**Sentiment:** {sentiment}")
        st.markdown(f"**Emotion:** {emotion}")
        st.markdown(f"**Polarity Score:** {polarity:.2f}")
        st.markdown(f"**Subjectivity Score:** {subjectivity:.2f}")
    else:
        st.warning("Please enter some text to analyze.")
