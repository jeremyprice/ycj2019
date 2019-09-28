---
layout: single
title:  "Vigenère Cipher"
date:   2019-09-27 11:00:00 -0500
categories: cryptography polyalphabetic cipher
---

We've done some simple shifting and substitutions for our ciphers, now lets add some more complexity.  A simple shift is easy to crack because once you know the shift distance for one of the letters you know the shift distance for all the letters.  What if we varied the shift distance for each letter?  Ciphers like this are called polyalphabetic ciphers because they involve using different keys (alphabets).

The polyalphabetic cipher we are going to learn about is the Vigenère cipher.  This cipher uses the Caesar cipher, but instead of one shift for all the characters it uses a different shift for each character.  The image below shows a Vigenère square and illustrates how each letter can be encoded using a different shift distance.

![Vigenère square](/images/Vigenère_square_shading.svg)

To use a Vigenère as our cipher we need one more piece: a keyword.  The way we choose which Caesar cipher to use for each letter is goverend by a keyword or phrase.  As an example, let's choose the keyword `code` to encode our message `apple`.  We use the `code` keyword by looking in the Vigenère square at the row `c` for the cipher for the first letter in our plaintext `a`.  We find the column that corresponds to the plaintext `a` and go down the rows until we get to the keyword letter `c`.  That gives us our ciphertext `c`.  What do we do if our plaintext is longer than our keyword?  We just repeat the keyword as many times as necessary.  Here is the full example (note that we repeated our keyword):
```
keyword:    codec
plaintext:  apple
ciphertext: cdspg
```



### todo hide/show the answer
This is the plaintext message: `Thanks for decrypting this`.  Did you get it right?

Now it is your turn:

1. Write a message that you want to encrypt.
2. Create a key you would like to use.  **Make sure each letter is used only once!**
3. Encrypt your message.
4. Pass it to the person with you and see if they can understand it.

Keep doing those steps until you feel like you understand the substitution cipher well.

[Click here to learn more about the Vigenère cipher.](https://en.wikipedia.org/wiki/Vigenère_cipher)
