import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import openai

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set your OpenAI API key here
api_key = "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"  # Replace with your ChatGPT API key

# Initialize the OpenAI API client
openai.api_key = api_key


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""  # Initialize the variable with an empty string

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('google', '')
                print(command)
    except sr.WaitTimeoutError:
        # Handle timeout error if needed
        pass
    except sr.RequestError:
        # Handle speech recognition request error if needed
        pass
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return command

# Initialize the ChatGPT conversation
messages = []


def run_gpt_voice():
    command = take_command()
    print(command)

    if 'play' in command:
        # Your existing code for playing music
        pass

    elif 'time' in command:
        # Your existing code for telling the time
        pass

    elif ('what is '
          ' ') in command:
        query = command.replace('what is  ', '')
        try:
            # Use ChatGPT to generate a response to the user's question
            messages.append({"role": "user", "content": query})
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            reply = chat.choices[0].message.content

            talk(f"According to my knowledge, {reply}")
            print(f"According to my knowledge, {reply}")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            talk("Sorry, an error occurred while generating a response.")

    elif 'date' in command:
        # Your existing code for handling date-related queries
        pass

    # Add other conditions for your existing functionality here

    else:
        talk('Please say the command again.')


while True:
    run_gpt_voice()
