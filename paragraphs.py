def dollarwords(input):
    ''' INSPIRATION FROM Because of Mr. Terupt BY Rob Buyea '''

    # SETUP
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letternumbers = []
    wordarray = []
    totalnumbers = 0
    dollar = "No"

    # GET INPUT
    word = input

    # VARS
    wordlength = len(word)
    alphalength = len(alphabet)
    word = word.lower()

    # INPUT TO ARRAY
    for i in range(wordlength):
        wordarray.append(word[i])

    # FIND NUMBER EQUIVALENTS OF LETTERS
    for i in range(0, wordlength):
        for j in range(0, alphalength):
            if wordarray[i] == alphabet[j]:
                j += 1
                letternumbers.append(j)

    # FIND TOTAL VALUE OF WORD
    for i in range(0, len(letternumbers)):
        totalnumbers += letternumbers[i]

    # OUTPUT
    if totalnumbers == 100:
        dollar = "Yes"
        print("word:                  ", word)
        print("total value:           ", totalnumbers)
        print("dollar word?            Yes")
        print("#############################")

paragraph = input("Enter paragraph here: ")

splitpara = paragraph.split()

for i in range(0, len(splitpara)):
    dollarwords(splitpara[i])
