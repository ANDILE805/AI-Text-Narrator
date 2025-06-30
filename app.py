import streamlit as st
import boto3

aws_access_key_id = st.secrets["aws"]["aws_access_key_id"]
aws_secret_access_key = st.secrets["aws"]["aws_secret_access_key"]
region_name = st.secrets["aws"]["region_name"]

polly = boto3.client(
    "polly",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

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
            response = polly.synthesize_speech(
                Text=text_input,
                OutputFormat='mp3',
                VoiceId=voice
            )


           audio_bytes = response['AudioStream'].read()

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

