# Welcome
Hello, world! Welcome to this repository. If you wish to encrypt or decrypt phrases, these programs are for you! Simply enter the words you wish to encrypt or decrypt in the corresponding program, and it'll will add up the total numbers of each word.

### What's a 'cipher'?
A cipher is a "code" -- a way of disguising, called "encrypting," words. 
Caesar cipher, substitution cipher, and pigpen cipher are some examples of ciphers.

## Files
### ```caesarcipher.py```
The Caesar cipher was first used by -- you guessed it -- Julius Caeser. This cipher involves shifting letters down the alphabet
by a predetermined number of letters. For example, if the number of letters to shift by (called the "key") is 3, then then the letter _a_
would become _d_, _b_ becomes _e_, _c_ becomes _f_, and so on. Some famous uses of the Caesar cipher include ROT13, where ```key = 13```, and the traditional ```key = 3``` that Julius Caesar himself used. Here's an example of how this program works:
```
Enter number of letters to shift by: 3
Enter phrase to encrypt or decrypt: This is an example of a Caesar cipher. This text will become unreadable when the program has shifted all letters three letters down.
Encrypt or decrypt (e/d)? e
-----------------------------------------------------------------------------------------------------------------------------------------------------------
| Encrypted message: Wklv lv dq hadpsoh ri d Fdhvdu flskhu. Wklv whaw zloo ehfrph xquhdgdeoh zkhq wkh surjudp kdv vkliwhg doo ohwwhuv wkuhh ohwwhuv grzq. |
-----------------------------------------------------------------------------------------------------------------------------------------------------------
```

### ```atbashcipher.py```
The Atbash cipher, also called the reverse alphabet or backwards cipher, is a type of substitution
cipher originally used for the Hebrew alphabet. For example, _a_ becomes _z_, _b_ becomes _y_, _c_ becomes _x_, and so on, all the way to _m_ = _n_ and _n_ = _m_. It may be of interest to note that the Atbash cipher is completely reversible; that is, decryption and encryption methods are exactly the same. This program encrypts and decrypts messages by the Atbash cipher. Here's an example of how it works:
```
Welcome to the Atbash Cipher Program!
This program will encrypt or decrypt your message using the Atbash cipher.
########################################
Enter message here: The quick brown fox jumped over the lazy dog.
Mode: encrypt or decrypt (e/d)? e
########################################
Encrypted message: Gsv jfrxp yildm ulc qfnkvw levi gsv ozab wlt.
########################################
```

## Conclusion
I hope these programs prove useful to you! Happy coding!
