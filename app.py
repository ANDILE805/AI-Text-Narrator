import streamlit as st
from narrator import synthesize_text_to_speech

st.set_page_config(
    page_title="Text Narrator App",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #FFDEE9, #B5FFFC);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #FF5E99;
        text-align: center;
        padding: 20px 0;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">AI Text Narrator 🎧</div>', unsafe_allow_html=True)
st.subheader("Turn your text into speech with fun & flair 💫")

text_input = st.text_area("✨ Type something awesome here:")
uploaded_file = st.file_uploader("📂 Or upload a .txt file to narrate", type=["txt"])

voice = st.selectbox("🎤 Choose a voice you vibe with", ["Joanna", "Matthew", "Ivy", "Brian", "Amy"])

if uploaded_file:
    text_input = uploaded_file.read().decode("utf-8")

if st.button("🎬 Let’s Narrate!"):
    if not text_input.strip():
        st.warning("Please enter or upload text to narrate ✍️")
    else:
        with st.spinner("Generating voice magic... 🎛️"):
            audio_bytes = synthesize_text_to_speech(text_input, voice)
            st.success("✅ Narration complete! Click below to listen 🎧")
            st.audio(audio_bytes, format='audio/mp3')

st.markdown('''
<div class="footer">
    Made with 💖 using Amazon Polly & Streamlit |
    <a href="https://github.com/ANDILE805/AI-Text-Narrator" target="_blank" style="text-decoration: none; color: #FF5E99;">
        Andile Mbatha
    </a>
</div>
''', unsafe_allow_html=True)


