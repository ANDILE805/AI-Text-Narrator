import boto3

polly = boto3.client('polly')

text = "Hello! This is your first narrated voice using Amazon Polly."

response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'  
)


with open('output.mp3', 'wb') as file:
    file.write(response['AudioStream'].read())
    

print("Narration saved as output.mp3")
