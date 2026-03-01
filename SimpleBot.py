"""
A simple chatbot that can greet the user, perform basic arithmetic, and respond to user input.

"""


def simple_bot():
    bot_name: str = "SimpleBot v1.0"
    print(f"Hello! I am {bot_name}. How can I assist you today?")

    while True:
        user_input: str = input("You: ").lower()
        if user_input in ['hi', 'hello']:
            print(f"{bot_name}: Hello there! How can I assist you today?")
        # added 'bye' to the list of exit commands
        elif user_input in ['exit', 'quit', 'bye']:
            print(f"{bot_name}: Goodbye! Have a great day!")
        elif user_input in ['+', 'add']:
            print(f"{bot_name}: Let me add two numbers for you.")
            try:
                num1 = float(input(f"{bot_name}: Enter the first number: "))
                num2 = float(input(f"{bot_name}: Enter the second number: "))
                print(f"{bot_name}: The sum of {num1} and {num2} is {num1 + num2}.")
            except ValueError:
                print(f"{bot_name}: Please enter valid numbers.")
        else:
            print(f"{bot_name}: You said '{user_input}'. That's interesting!")


if __name__ == "__main__":
    simple_bot()
