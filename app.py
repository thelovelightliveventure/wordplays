# SETUP
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
letternumbers = []
wordarray = []
totalnumbers = 0
dollar = "No"

# GET INPUT
word = input("Enter any word: ")

# VARS
wordlength = len(word)
alphalength = len(alphabet)

# INPUT TO ARRAY
for i in range(wordlength):
    wordarray.append(word[i])

# FIND NUMBER EQUIVALENTS OF LETTERS
for i in range(0, wordlength):
    for j in range(0, alphalength):
        if wordarray[i] == alphabet[j]:
            j += 1
            letternumbers.append(j)
    if wordarray[i] == "y":
        letternumbers.append(25)

# FIND TOTAL VALUE OF WORD
for i in range(0, len(letternumbers)):
    totalnumbers += letternumbers[i]

# DOLLAR WORD?
if totalnumbers == 100:
    dollar = "Yes"
else:
    dollar = "No"

# OUTPUT
print("word:                  ", word)
print("# of letters:          ", wordlength)
print("word array:            ", wordarray)
print("values of each letter: ", letternumbers)
print("total value:           ", totalnumbers)
print("dollar word?           ", dollar)
