#Local implementation for both `OPENING PART` & `CLOSING PART` 
#Input is Hindi 
#Input will be Elvenlabs API, Sender & Receiver Names
#then, give the final text before generating audio
#generate the audio

import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

tts_client = ElevenLabs(api_key=elevenlabs_api_key)

# Function to generate and save TTS audio
def generate_audio(ssml_text, filename):
    response_generator = tts_client.text_to_speech.convert(
        voice_id="2F1KINpxsttim2WfMbVs",
        output_format="mp3_44100_128",
        text=ssml_text,
        model_id="eleven_multilingual_v2",
    )
    with open(filename, "wb") as file:
        for chunk in response_generator:
            file.write(chunk)
    print(f"Audio saved as: {filename}")

receiver_name_hindi = input("Receiver Name (in Hindi): ")
sender_name_hindi = input("Sender Name (in Hindi): ")

# Opening Part SSML
opening_text = f"Hi {receiver_name_hindi}, ध्वनि भानुशाली here! Closeup & I have a very special Valentine's Day surprise for you from {sender_name_hindi}. It’s a song dedicated to you, and I'm so excited to sing it! I hope you love it."
opening_ssml = f"""
<speak>
    Hi {receiver_name_hindi}, ध्वनि भानुशाली here! <break time="500ms"/>
    Closeup & I have a very special Valentine's Day surprise for you from {sender_name_hindi}. <break time="500ms"/>
    It’s a song dedicated to you, <prosody rate="slow" pitch="low" volume="medium" emotion="romantic">
    and <prosody duration="3s" emotion="joyful">I'm so excited</prosody>
    <prosody duration="3s" emotion="playful">to sing it!</prosody></prosody>
    <break time="500ms"/> I hope you love it.
</speak>
"""

# Closing Part SSML
closing_text = f"This Valentine's Day, {receiver_name_hindi} और {sender_name_hindi}, Close Up के साथ, पास आओ ना."
closing_ssml = f"""
<speak>
    <p> <prosody rate="slow" pitch="low"> <emphasis level="strong">This Valentine's Day,</emphasis> </prosody> </p>
    <p> <prosody rate="slow" pitch="medium"> <break time="300ms"/> <prosody volume="soft"> {receiver_name_hindi} और {sender_name_hindi},</prosody> <break time="200ms"/> </prosody> </p>
    <p> <prosody rate="slow" pitch="low"> <emphasis level="moderate">Close Up के साथ,</emphasis> </prosody> </p>
    <p> <prosody rate="slow" pitch="low"> <break time="400ms"/> <emphasis level="strong">पास</emphasis> <break time="300ms"/> <emphasis level="moderate">आओ</emphasis> <break time="300ms"/> <emphasis level="strong">ना.</emphasis> </prosody> </p>
</speak>
"""

# Generate and save separate audio files
generate_audio(opening_ssml, "opening_part_audio.mp3")
generate_audio(closing_ssml, "closing_part_audio.mp3")

# Display Final Translated Text
print("\n Final Text Before Generating Audio:")
print("\n🎤 Opening Part:")
print(opening_text)

print("\n🎤 Closing Part:")
print(closing_text)

print("\n🎧 Audio files generated successfully!")
