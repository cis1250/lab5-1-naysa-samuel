#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        text = input("Please enter a sentence: ")
        if is_sentence(text):
            return text
        else:
            print("Error: Invalid sentence. Please try again.")

def compute_word_frequencies(sentence):
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', sentence.lower())
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def print_word_frequencies(frequency):
    print("Word Frequencies:")
    for word, count in frequency.items():
        print(f"{word}: {count}")

def main():
    sentence = get_sentence()
    frequency = compute_word_frequencies(sentence)
    print_word_frequencies(frequency)

if __name__ == "__main__":
    main()
