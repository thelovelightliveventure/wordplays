# Welcome to ```wordplays```!
Hello, world! This is a repository filled with my projects related to wordplay. If you're interested in using 
Python to find special words, such as dollar words and heterograms, or to encrypt phrases, you're in the right place!

# Projects
- dollarwords
- heterograms
- ciphers
## ```dollarwords```
### What's a 'dollar word'?
A dollar word is a word whose numeric counterparts add up to 100, with "a" being 1, "b" being 2, and so on. *Molecular*, for example,
is a dollar word: 13(m) + 15(o) + 12(l) + 5(e) + 3(c) + 21(u) + 12(l) + 1(a) + 18(r) = 100! Dollar words are not case-sensitive.
### Files
- ```word.py```: processes one word at a time and gives information about the word,
returning any kind of words - even those that are not dollar words.
- ```paragraphs.py```: processes paragraphs (or even chapters!) at a time, returning only dollar words.
- ```targetwords.py```: checks for words matching user input of target sum, instead of only checking for dollar words. Functions like paragraph.py

## ```heterograms```
### What's a 'heterogram'?
A heterogram is a word that has no repeat characters. For example, _pathfinder_, _background_, and _bankrupt_ are heterograms, because those words do not have any repeating characters. However, _thumbtacks_ would not be a heterogram, because the letter _t_ is repeated. Heterograms are not case-sensitive.
### Files
- ```heterograms.py```: processes paragraphs at a time and returns only heterograms with lengths above a user-specified word length.

## ```ciphers```
### What's a 'cipher'?
A cipher is a "code" -- a way of disguising, called "encrypting," words. Caesar cipher, substitution cipher, and pigpen cipher are some examples of ciphers.
### Files
- ```caesarcipher.py```: processes phrases or paragraphs at a time, shifting the letters by a user-inputted number of letters. For example, if the key, or number of letters to shift by, is ```3```, then the letter _a_ would become _d_, _b_ becomes _e_, _c_ becomes _f_, and so on.
- ```atbashcipher.py```: processes phrases or paragraphs at a time, reversing the alphabet. For example, _a_ becomes _z_, _b_ becomes _y_, _c_ becomes _x_, and so on, all the way to _m_ = _n_ and _n_ = _m_. 

# Conclusion
I hope these programs prove useful (or at least somewhat entertaining) to you! Happy coding!
