import pyttsx3
import openai
import speech_recognition as sr

# Set Your Open AI key
openai.api_key = "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"

engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except Exception as e:
        print(f'Error during transcription: {str(e)}')

def generate_response(prompt):
    friendly_prompt = f"Please provide an explanation of '{prompt}' in a conversational and friendly tone suitable for a trainer to narrate to students."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=friendly_prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        # Wait for the user to provide input (voice or text)
        user_input = input("Type your question or say 'genius' to start voice input: ")

        if user_input.lower() == "genius":
            # Use voice recognition
            print("Say 'genius' to start recording your question")
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                audio = recognizer.listen(source)
                try:
                    transcription = recognizer.recognize_google(audio)
                    text = transcribe_audio_to_text("input.wav")
                    if text:
                        print(f"You said: {text}")
                        response = generate_response(text)
                        print(f"GPT-3 says: {response}")
                        speak_text(response)
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
        else:
            # Use the provided text message
            text = user_input
            print(f"You typed: {text}")
            response = generate_response(text)
            print(f"GPT-3 says: {response}")
            speak_text(response)

if __name__ == "__main__":
    main()
