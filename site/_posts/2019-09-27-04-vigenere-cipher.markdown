---
layout: single
title:  "Vigenère Cipher"
date:   2019-09-27 11:00:00 -0500
categories: cryptography polyalphabetic cipher
---

We've done some simple shifting and substitutions for our ciphers, now lets add some more complexity.  A simple shift is easy to crack because once you know the shift distance for one of the letters you know the shift distance for all the letters.  What if we varied the shift distance for each letter?  Ciphers like this are called polyalphabetic ciphers because they involve using different keys (alphabets).

The polyalphabetic cipher we are going to learn about is the Vigenère cipher.  This cipher uses the Caesar cipher, but instead of one shift for all the characters it uses a different shift for each character.  The image below shows a Vigenère square and illustrates how each letter can be encoded using a different shift distance.

![Vigenère square](/ycj/images/Vigenere_square_shading.svg)

To use a Vigenère as our cipher we need one more piece: a keyword.  The way we choose which Caesar cipher to use for each letter is goverend by a keyword or phrase.  As an example, let's choose the keyword `code` to encode our message `apple`.  We use the `code` keyword by looking in the Vigenère square at the row `c` for the cipher for the first letter in our plaintext `a`.  We find the column that corresponds to the plaintext `a` and go down the rows until we get to the keyword letter `c`.  That gives us our ciphertext `c`.  What do we do if our plaintext is longer than our keyword?  We just repeat the keyword as many times as necessary.  Here is the full example (note that we repeated our keyword):
```
keyword:    codec
plaintext:  apple
ciphertext: cdspg
```

Now it is your turn to try it.  Encode the following plaintext using the keyword below.
```
keyword:   secret
plaintext: I love this cipher!
```

### todo hide/show the answer
This is the ciphertext message: `A nfzx xjzw umryik!`.  Did you get it right?

Notice that unlike the substitution ciphers we worked with, the Vigenère cipher requires us to have a keyword that everyone in our secret club needs to know.  This is referred to as a pre-shared key meaning that we have to share the key before we start sending and receiving messages.

The decryption of the message looks very similar to the encryption.  We still need our keyword, but instead of using the column that is associated with the letter we are decrypting we find the letter in the row and look up to the letter at the top of the column.  Try it with one of the examples we did for the encryption.  Can you decrypt the ciphertext and get the plaintext?

Try to decrypt this encrypted message:
```
keyword:    youthcodejam
ciphertext: G bhwg L moz'h kbp ryc ad nbtg
```

### todo hide/show the answer
This is the plaintext message: `I hope I don't run out of time`.  Did you get it right?

Now it is your turn:

1. Write a message that you want to encrypt.
2. Create a keyword you would like to use.
3. Encrypt your message.
4. Pass the message and the keyword to the person with you and see if they can understand it.

Keep doing those steps until you feel like you understand the substitution cipher well.

[Click here to learn more about the Vigenère cipher.](https://en.wikipedia.org/wiki/Vigenère_cipher)
