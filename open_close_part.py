#Streamlit implementation for both `OPENING PART` & `CLOSING PART` 
#Input is Hindi 
#Input will be Elvenlabs API, Sender & Receiver Names
#then, give the final text before generating audio
#generate the audio

import streamlit as st
from elevenlabs import ElevenLabs

# Streamlit UI
st.title("🎧 CloseUp Audio TTS Generator")
st.sidebar.header("Select an Option")

# Sidebar options
option = st.sidebar.radio("Choose an option:", ["Opening Part", "Closing Part", "Opening + Closing Part"])

# User inputs API Key
elevenlabs_api_key = st.text_input("Enter your ElevenLabs API Key", type="password")

receiver_name_hindi = st.text_input("Enter Receiver's Name (Hindi)")
sender_name_hindi = st.text_input("Enter Sender's Name (Hindi)")

# Function to generate and save TTS audio
def generate_audio(ssml_text, filename):
    tts_client = ElevenLabs(api_key=elevenlabs_api_key)
    response_generator = tts_client.text_to_speech.convert(
        voice_id="2F1KINpxsttim2WfMbVs",
        output_format="mp3_44100_128",
        text=ssml_text,
        model_id="eleven_multilingual_v2",
    )
    with open(filename, "wb") as file:
        for chunk in response_generator:
            file.write(chunk)
    return filename

if st.button("Generate Audio"):
    if not elevenlabs_api_key:
        st.warning("⚠️ Please enter your ElevenLabs API Key.")
    elif not receiver_name_hindi or not sender_name_hindi:
        st.warning("⚠️ Please enter both sender and receiver names")
    else:
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

        # Generate audio based on selection
        if option == "Opening Part":
            st.subheader("🎤 Opening Part")
            st.write(opening_text)
            opening_audio = generate_audio(opening_ssml, "opening_part_audio.mp3")
            st.audio(opening_audio, format="audio/mp3")

        elif option == "Closing Part":
            st.subheader("🎤 Closing Part")
            st.write(closing_text)
            closing_audio = generate_audio(closing_ssml, "closing_part_audio.mp3")
            st.audio(closing_audio, format="audio/mp3")

        elif option == "Opening + Closing Part":
            st.subheader("🎤 Opening Part")
            st.write(opening_text)
            opening_audio = generate_audio(opening_ssml, "opening_part_audio.mp3")
            st.audio(opening_audio, format="audio/mp3")

            st.subheader("🎤 Closing Part")
            st.write(closing_text)
            closing_audio = generate_audio(closing_ssml, "closing_part_audio.mp3")
            st.audio(closing_audio, format="audio/mp3")
