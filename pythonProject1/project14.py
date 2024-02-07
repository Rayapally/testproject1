import openai

# Set Your Open AI key
openai.api_key = "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"

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

def main():
    while True:
        # Display a menu of options to the user
        print("Choose an option:")
        print("1. Black Box Testing")
        print("2. White Box Testing")
        print("3. Other")
        print("4. Quit")

        # Get the user's choice
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            text = "Tell me about Black Box Testing"
        elif choice == "2":
            text = "Tell me about White Box Testing"
        elif choice == "3":
            text = input("Type your question: ")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        # Generate Response
        response = generate_response(text)

        # Print the response in text
        print(f"GPT-3 says: {response}")

if __name__ == "__main__":
    main()
