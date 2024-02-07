import openai
import threading
import os
from gtts import gTTS
from pygame import mixer

# Set your OpenAI API key
openai.api_key = "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"


def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)


def save_text_and_speech(text, filename):
    print(text)

    # Save the text to a file
    with open(filename + ".txt", 'w', encoding='utf-8') as file:
        file.write(text)

    # Convert text to speech and save it as an MP3 file
    tts = gTTS(text=text, lang='en')
    tts.save(filename + ".mp3")


def main():
    counter = 1
    while True:
        # Display a menu of options to the user
        print("Choose an option:")
        print("1. Black Box Testing")
        print("2. White Box Testing")
        print("3. Unit Testing")
        print("4. Quit")

        # Get the user's choice
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            topic = "Black Box Testing"
        elif choice == "2":
            topic = "White Box Testing"
        elif choice == "3":
            topic = "Unit Testing"
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        # Create a prompt with the chosen topic
        prompt = f"Please provide an explanation of {topic} in a conversational and friendly tone suitable for a trainer to narrate to students."

        # Generate Response
        response = generate_response(prompt)

        # Save the response as both text and speech (MP3)
        filename = f"response_{counter}"
        save_text_and_speech(response, filename)

        # Play the generated speech
        mixer.init()
        mixer.music.load(filename + ".mp3")
        mixer.music.play()

        counter += 1


if __name__ == "__main__":
    main()
