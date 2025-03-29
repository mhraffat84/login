def ChatBOT():
    print("Hello, I am your ChatBOT!, Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower() # convert user input to lowercase

        if user_input == 'exit': # exit if user types 'exit'
            print("ChatBOT: Goodbye!")
            break   # to quit the app
        
        elif "hello" in user_input: # if user types 'hello' in the meesage
            print("ChatBOT: Hello! How can I help you?")
        
        elif "how are you" in user_input: # if user types 'how are you' in the meesage
            print("ChatBOT: I am a computer program, I don't have feelings. But thanks for asking!")
        
        elif "your name" in user_input: # if user types 'your name' in the meesage
            print("ChatBOT: I am ChatBOT!")
        
        else: #if user types anything else
            print("ChatBOT: I am not programmed to answer that question.")
            print("ChatBOT: Please ask me something else.")

# Call the function
ChatBOT()