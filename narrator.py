import streamlit as st
import boto3

def synthesize_text_to_speech(text, voice='Joanna'):
   
    aws_access_key_id = st.secrets["aws"]["aws_access_key_id"]
    aws_secret_access_key = st.secrets["aws"]["aws_secret_access_key"]
    region_name = st.secrets["aws"]["region_name"]

 
    polly = boto3.client(
        "polly",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )


    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice
    )
    
  
    audio_bytes = response['AudioStream'].read()
    return audio_bytes
