# Welcome
Welcome to this repository! If you wish to find "dollar words", this program is for you! Simply enter the words you wish to check,
and the program will add up the total numbers of each word.

### What's a 'dollar word'?
A dollar word is a word whose numeric counterparts add up to 100, with "a" being 1, "b" being 2, and so on. *Molecular*, for example,
is a dollar word: 13(m) + 15(o) + 12(l) + 5(e) + 3(c) + 21(u) + 12(l) + 1(a) + 18(r) = 100! Dollar words are not case-sensitive.

## Files
```word.py``` processes one word at a time and gives more information about the word, returning any kind of words - even those that are not dollar words.
Here's an example:

```
word:                   goldendoodle
# of letters:           12
word array:             ['g', 'o', 'l', 'd', 'e', 'n', 'd', 'o', 'o', 'd', 'l', 'e']
values of each letter:  [7, 15, 12, 4, 5, 14, 4, 15, 15, 4, 12, 5]
total value:            112
dollar word?            No
```

```paragraphs.py```, on the other hand, can process chapters at a time, returning only dollar words.
Here's an example (the input is the third chapter of *Pride and Prejudice*:

```
Enter paragraph here: Mr. Bennet was among the earliest of those who waited on Mr. Bingley. He had always intended to visit him,
though to the last always assuring his wife that he should not go; and till the evening after the visit was paid
she had no knowledge of it. It was then disclosed in the following manner. Observing his second daughter employed in trimming a hat,
he suddenly addressed her with: “I hope Mr. Bingley will like it, Lizzy.” “We are not in a way to know what Mr. Bingley likes,”
said hermother resentfully, “since we are not to visit.” “But you forget, mamma,” said Elizabeth, “that we shall meet him at the
assemblies, and that Mrs. Long promised to introduce him.” “I do not believe Mrs. Long will do any such thing. She has two nieces of her
own. She is a selfish, hypocritical woman, and I have no opinion of her.” “No more have I,” said Mr. Bennet; “and I am glad to find
that youdo not depend on her serving you.” Mrs. Bennet deigned not to make any reply, but, unable to contain herself, began scolding
one of her daughters. “Don’t keep coughing so, Kitty, for Heaven’s sake! Have a little compassion on my nerves. You tear them to pieces.”
“Kitty has no discretion in her coughs,” said her father; “she times them ill.”“I do not cough for my own amusement,” replied Kitty
fretfully. “When is your next ball to be, Lizzy?” “To-morrow fortnight.” “Aye, so it is,” cried her mother, “and Mrs. Long does
not come3back till the day before; so it will be impossible for her to introduce him, for she will not know him herself.” “Then, my dear,
you may have the advantage of your friend, and introduce Mr. Bingley to her.” “Impossible, Mr. Bennet, impossible, when I am not
acquainted with him myself; how can you be so teasing?” “I honour your circumspection. A fortnight’s acquaintance is certainly very
little. One cannot know what a man really is by the end ofa fortnight. But if we do not venture somebody else will; and after all,
Mrs. Long and her daughters must stand their chance; and, therefore, as she will think it an act of kindness, if you decline the office,
I will take it on myself.” The girls stared at their father. Mrs. Bennet said only, “Nonsense, nonsense!” “What can be the meaning of
that emphatic exclamation?” cried he. “Do you consider the forms of introduction, and the stress that is laid on them, as nonsense?
I cannot quite agree with you there. What say you, Mary? For you are a young lady of deep reflection, I know, and read great books and
make extracts.” Mary wished to say something sensible, but knew not how. “While Mary is adjusting her ideas,” he continued,
“let us return to Mr. Bingley.” “I am sick of Mr. Bingley,” cried his wife. “I am sorry to hear that; but why did not you tell me
that before? If Ihad known as much this morning I certainly would not have called on him. It is very unlucky; but as I have actually
paid the visit, we cannot escape the acquaintance now.” The astonishment of the ladies was just what he wished; that of Mrs. Bennet
perhaps surpassing the rest; though, when the first tumult of joy was over, she began to declare that it was what she had expected all
the while. “How good it was in you, my dear Mr. Bennet! But I knew I should persuade you at last. I was sure you loved your girls
too well to neglect such an acquaintance. Well, how pleased I am! and it is such a good joke, too, that you should have gone this morning
and never said a word about it till now.” “Now, Kitty, you may cough as much as you choose,” said Mr. Bennet; and, as he spoke,
he left the room, fatigued with the raptures of his wife. “What an excellent father you have, girls!” said she, when the doorwas shut.
“I do not know how you will ever make him amends for his kindness; or me, either, for that matter. At our time of life it is not so
pleasant, I can tell you, to be making new acquaintances every day; but for your sakes, we would do anything. Lydia, my love, though
you are the youngest, I dare say Mr. Bingley will dance with you at the nextball.” “Oh!” said Lydia stoutly, “I am not afraid;
for though I am the youngest, I’m the tallest.” The rest of the evening was spent in conjecturing how soon he would return Mr. Bennet’s
visit, and determining when they should ask him to dinner.
word:                   therefore
total value:            100
dollar word?            Yes
#############################                   
word:                   stress
total value:            100
dollar word?            Yes
#############################
word:                   excellent
total value:            100
dollar word?            Yes
#############################
```

## Conclusion
I hope this program proves useful to you! Happy coding!
