"""
    Analyze if a word matches the target sum
    Inspired by dollarwords from Because of Mr. Terupt
"""

# SETUP
def wordanalysis(word):
    return sum((ord(char) - ord('a') + 1) for char in word.lower() if char.isalpha()) 

def find_matching_words(targetNum, paragraph):
    targetNum = int(targetNum)
    words = paragraph.split()
    match_set = set()

    for word in words:
        word_value = wordanalysis(word)
        if word_value == targetNum and word not in match_set:
            match_set.add(word)
            print(f"word:                  {word}")
            print(f"total value:           {word_value}")
            print(f"target word?            Yes")
            print(f"#############################")
    
    if not match_set:
        print("No matches found.")

def main():
    # GET USER INPUT
    try:
        targetNum = int(input("Enter desired sum: "))
        paragraph = input("Enter paragraph here: ")
    except ValueError:
        print("Invalid input. Please enter a number for the target sum.")
        return
    
    if not paragraph.strip():
        print("No words entered. Please try again.")
        return

    # PROCESS WORDS
    find_matching_words(targetNum, paragraph)

if __name__ == "__main__":
    main()
