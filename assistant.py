print("Voice Assistant Started")

while True:
    command = input("You: ").lower()

    if command == "hello":
        print("Assistant: Hello!")

    elif command == "open youtube":
        print("Assistant: Opening YouTube")
        print("https://youtube.com")

    elif command == "open google":
        print("Assistant: Opening Google")
        print("https://google.com")

    elif command == "stop":
        print("Assistant: Goodbye")
        break

    else:
        print("Assistant: Sorry, I didn't understand")