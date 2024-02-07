import speech_recognition as sr
import pyttsx3
import openai
import time

# Set Your Open AI key333
openai.api_key = "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"

engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]


def generate_friendly_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    friendly_response = response["choices"][0]["text"]

    # Add a friendly greeting or acknowledgment
    friendly_response = "Hello! Have a nice day " + friendly_response

    return friendly_response


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        # Wait for the user to say "genius" within a certain timeout
        print("Say 'genius' to start recording your question")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            try:
                audio = recognizer.listen(source, timeout=5)  # Adjust the timeout as needed
                transcription = recognizer.recognize_google(audio)

                if transcription.lower() == "genius":
                    # Record Audio
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                            # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"you said: {text}")

                        # Generate Response
                        response = generate_response(text)
                        print(f"GPT-3 says: {response}")

                        # Read Response Using Text-to-Speech
                        speak_text(response)

            except sr.WaitTimeoutError:
                print("Timeout reached. You didn't say 'genius' within the specified time.")
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
