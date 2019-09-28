---
layout: single
title:  "Shift Cipher"
date:   2019-09-27 10:00:00 -0500
categories: cryptography shift cipher
---

The shift cipher is a very common cipher that is easy to understand, easy to encrypt and decrypt, but provides a basic level of security for your message.  Essentially, a shift cipher requires that we take each letter in our source message and shift it by a specified amount.  This cipher is sometimes referred to as a Caesar Cipher.


![example shift cipher](/ycj/images/Caesar_cipher_left_shift_of_3.svg)
Here is an example of the shift cipher.  For this example, we chose a left shift of 3 for each letter (often represented as a distance of `-3`).  Thus, each occurrence of the letter `E` in the plaintext message becomes the letter `B` in the ciphertext message.

If we encrypt a message using the left shift of 3 example you see above it would look something like this:
```
Really important message contained herein
Obxiiv fjmloqxkq jbppxdb zlkqxfkba ebobfk
```

Now it is your turn.  The message below is encrypted using a shift of 2.  Can you decrypt the message?

`vguv oguucig`

<button onclick="showHide('plaintext1')">Click here to see the answer</button>
<div id="plaintext1" style="display: none;
    box-sizing: border-box;
    background-color: #000;
    position: relative;
    margin-bottom: 1em;
    background: #263238;
    color: #eeffff;
    font-size: 0.75em;
    line-height: 1.8;
    border-radius: 4px;
    padding: 1em;">
This is the plaintext message:<br>
<code class="highlighter-rouge">test message</code><br>
Did you get it right?
</div>

What happened to the space in that message?  Did our encryption change it at all?  What do you think we should do with other punctuation?  For a shift cipher we ignore any characters that aren't alphabetical (a-z).  Any punctuation or whitespace is copied verbatim from the plaintext message to the ciphertext message.
Also, each ciphertext character is the same case as the plaintext character.  For instance, a capital letter in plaintext will result in a capital letter in the ciphertext.

Let's try a negative shift.  A negative shift makes us shift to the left instead of to the right.  The following message has a shift distance of `-5`.  Can you decode the message?

`Ocdn hznnvbz dni'o izbvodqz`

<button onclick="showHide('plaintext2')">Click here to see the answer</button>
<div id="plaintext2" style="display: none;
    box-sizing: border-box;
    background-color: #000;
    position: relative;
    margin-bottom: 1em;
    background: #263238;
    color: #eeffff;
    font-size: 0.75em;
    line-height: 1.8;
    border-radius: 4px;
    padding: 1em;">
This is the plaintext message:<br>
<code class="highlighter-rouge">this message isn't negative</code><br>
Did you get it right?
</div>

A handy tool you can use to implement a shift cipher is a code wheel (very similar to a secret decoder ring).  [Here is a cool one that you can use on the internet](http://inventwithpython.com/cipherwheel/){:target="_blank_"}  **Note: it doesn't work in a mobile browser.**

Our work so far has been decrypting messages using the shift cipher, but that's only half the work.  Here are some messages for you to encrypt.  The number in front of each message indicates the shift distance.  Can you figure out what the ciphertext looks like?
`7`:`Hello World!`<br>
`-4`: `Goodbye World?`

<button onclick="showHide('plaintext3')">Click here to see the answer</button>
<div id="plaintext3" style="display: none;
    box-sizing: border-box;
    background-color: #000;
    position: relative;
    margin-bottom: 1em;
    background: #263238;
    color: #eeffff;
    font-size: 0.75em;
    line-height: 1.8;
    border-radius: 4px;
    padding: 1em;">
<code class="highlighter-rouge">Olssv Dvysk!</code><br>
<code class="highlighter-rouge">Ckkzxua Sknhz?</code><br>
</div>

Now it is your turn:

1. Write a message that you want to encrypt.
2. Choose a shift distance you would like to use.
3. Encrypt your message.
4. Pass it to the person with you and see if they can understand it.

Keep doing those steps until you feel like you understand the shift cipher well.

[Click here to learn more about shift ciphers.](https://en.wikipedia.org/wiki/Caesar_cipher)

<script>
function showHide(elId) {
  var x = document.getElementById(elId);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>
