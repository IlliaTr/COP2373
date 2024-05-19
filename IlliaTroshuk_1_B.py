# Magic 8-Ball Simulator

import random


# Function to create the file with Magic 8 Ball responses
def create_responses_file():
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]
    with open("8ball_responses.txt", "w") as file:
        for response in responses:
            file.write(response + "\n")


# Function to read responses from file into a list
def read_responses():
    responses = []
    with open("8ball_responses.txt", "r") as file:
        for line in file:
            responses.append(line.strip())
    return responses


# Function to simulate Magic 8 Ball
def magic_8_ball():
    responses = read_responses()
    while True:
        input("Ask a yes/no type question: ")
        print(random.choice(responses))
        choice = input("Do you want to ask another question? (yes/no): ")
        if choice.lower() != "yes":
            break


# Main function
def main():
    create_responses_file()
    magic_8_ball()


# Execute the main function
if __name__ == "__main__":
    main()
