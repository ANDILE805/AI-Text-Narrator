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

polly = boto3.client('polly', region_name='us-east-1')


text = "Hello! This is your first narrated voice using Amazon Polly."

response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'  
)


with open('output.mp3', 'wb') as file:
    file.write(response['AudioStream'].read())
    

print("Narration saved as output.mp3")
