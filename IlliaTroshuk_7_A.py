# Sentence Splitter

import re

def split_sentences(text):
    # Create regex pattern to handle various sentence structures
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(pat, text, flags=re.DOTALL | re.MULTILINE)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def main():
    # Get user input
    text = input("Please enter the text: ")

    # Split sentences from user input
    sentences = split_sentences(text)

    # Display the sentences and the count
    for i, sentence in enumerate(sentences, start=1):
        print(f"Sentence {i}: {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()
