""" Heterograms are words where no letters repeat. This program finds heterograms 
from a given paragraph and lists them out. """

import string

def wordanalysis(word):
    """ Analyze words for repeat characters."""
    match = set()
    for char in word:
        if char in match:
            return False
        match.add(char)
    return True

def find_heterograms(min_length, paragraph):
    """Find and list heterograms that meet the minimum lengths."""
    # Format paragraph by removing punctuation and converting to lowercase
    words = paragraph.lower().translate(str.maketrans("", "", string.punctuation)).split()
    heterograms_found = False

    # Iterate through the words and print heterograms
    for word in words:
        # Check if word is a heterogram and meets minimum length requirement
        if wordanalysis(word) and len(word) >= min_length:
            print(f"Word:               {word}")
            print(f"Heterogram:         Yes")
            print("###################################")
            heterograms_found = True

    # If no heterograms found
    if not heterograms_found:
        print("No matches found.")

def main():
    """Main function to get user input and process the paragraph."""  
    try:
        # Get minimum length of word and paragraph
        min_length = int(input("Enter the minimum number of letters: "))
        paragraph = input("Enter paragraph here: ").strip()
        
        # If no input is entered for the paragraph
        if not paragraph:
            print("No words entered. Please try again.")
            return
        
        print("###################################")
        # Call the function to find heterograms
        find_heterograms(min_length, paragraph) 
    except ValueError:
        print("Invalid value. Please enter an integer.")

if __name__ == "__main__":
    main()
