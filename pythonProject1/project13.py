import openai
import speech_recognition as sr

# Set Your Open AI key
openai.api_key = "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"


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


def main():
    while True:
        # Wait for the user to provide input (text only)
        user_input = input("Type your question: ")

        # Use the provided text message
        text = user_input
        print(f"You typed: {text}")

        # Generate Response
        response = generate_response(text)

        # Print the desired output format
        output_message = f"Please provide an explanation of '{text}' in a conversational and friendly tone suitable for a trainer to narrate to students."
        print(output_message)


if __name__ == "__main__":
    main()
