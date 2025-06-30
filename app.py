import streamlit as st
import boto3

# Debug: confirm secrets are loaded
st.write("AWS Key starts with:", st.secrets["aws"]["aws_access_key_id"][:4])

# Create Polly client with credentials from secrets
polly = boto3.client(
    "polly",
    aws_access_key_id=st.secrets["aws"]["aws_access_key_id"],
    aws_secret_access_key=st.secrets["aws"]["aws_secret_access_key"],
    region_name=st.secrets["aws"]["region_name"]
)

st.title("🎤 Simple Text Narrator with Amazon Polly")

text = st.text_area("Enter text to narrate:")

voice = st.selectbox("Choose voice:", ["Joanna", "Matthew", "Ivy", "Brian", "Amy"])

if st.button("Narrate"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Generating speech..."):
            try:
                response = polly.synthesize_speech(
                    Text=text,
                    OutputFormat="mp3",
                    VoiceId=voice
                )
                audio_bytes = response['AudioStream'].read()
                st.audio(audio_bytes, format="audio/mp3")
                st.success("Done! Listen above.")
            except Exception as e:
                st.error(f"Error: {e}")



