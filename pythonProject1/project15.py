import openai

# Set Your Open AI key
openai.api_key = "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"

def generate_response(prompt):
    max_response_length = 4000  # Set a maximum response length
    response = ""
    remaining_prompt = prompt

    while remaining_prompt:
        # Request a response for a portion of the prompt
        response_chunk = openai.Completion.create(
            engine="text-davinci-003",
            prompt=remaining_prompt[:max_response_length],
            max_tokens=max_response_length,
            n=1,
            stop=None,
            temperature=0.5
        )
        response += response_chunk["choices"][0]["text"]

        # Remove the processed portion from the remaining prompt
        remaining_prompt = remaining_prompt[max_response_length:]

    return response

# Rest of your code...


def main():
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
        prompt = f"Please provide an explanation of {topic} testing in a conversational and friendly tone suitable for a trainer to narrate to students."

        # Generate Response
        response = generate_response(prompt)

        # Print the response in text with the chosen topic
        print(f"GPT-3  {prompt}: {response}")

if __name__ == "__main__":
    main()
