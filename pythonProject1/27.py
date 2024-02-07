import openai
import threading
import os
from gtts import gTTS
from pygame import mixer
import time
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# Set your Bard API key and endpoint
openai.api_key = "AIzaSyDjG3rU6dhRxr_m1V6_TsITSYgJVWl06L8"
bard_endpoint = "https://api.openai.com/v1/bard/completions"  # Replace with the correct Bard endpoint

# Initialize the Pygame mixer for audio playback
mixer.init()

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the Bard engine (replace with the correct engine name)
            prompt=prompt,
            max_tokens=150,  # Adjust the max_tokens parameter as needed
            n=1,
            stop=None,
            temperature=0.7,  # Adjust the temperature parameter as needed
            endpoint=bard_endpoint
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# ... (rest of your code remains unchanged)

if __name__ == "__main__":
    main()
