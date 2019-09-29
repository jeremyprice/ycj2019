---
layout: single
title:  "Base64 Encoding"
permalink: /base64.html
---

This algorithm isn't technically an encryption/decryption algorithm, but it does allow us to encode information so it can be more easily encrypted.  Base64 encoding is a technique we can use to turn a stream of arbitrary data (not just letters) into letters and numbers.  Sometimes we need to do this in order to send the information without it getting lost or misinterpreted.  It can also be used as a first step to encode our information before we encrypt it.

The first thing to understand about Base64 encoding is that we will be dealing with binary numbers.  If you don't know about binary numbers, I suggest you read [this Wikipedia article](https://en.wikipedia.org/wiki/Binary_number) on binary numbers and [this Wikipedia article](https://en.wikipedia.org/wiki/Binary_code) on binary code and make sure it makes sense before you move on.

The core premise behind Base64 encoding is that a series of characters in the message is really just a continuous stream of 1s and 0s.  Usually, we look at those 1s and 0s in 8-bit chunks and interpret the value as a character [see the ASCII chart for more info](https://en.wikipedia.org/wiki/ASCII).  With Base64 we put three of those 8-bit values together (giving us 24-bits total) and look at them as four 6-bit values.  Since 6-bit values are hard for humans to read and understand, we need to come up with a representation for each 6-bit value that will be easy to use.  Below is a table that shows how we are going to represent our 6-bit values.

![Base64 index table](/ycj/images/base64_index_table.png)

To use the table, we look for the 6-bit binary value we need to represent and then look over at the Char in that row.  Thus, if we want to encode the values `010110` and `111000` the Chars would be `W` and `4` respectively.  Note that the table has both lowercase and uppercase letters so you need to make sure you pay attention to the case.

Let's look at an example of how we would encode a message into base64.  The example word we will use is `Man`:
![Base64 word example](/ycj/images/base64_word_example.png)

Notice how we took 3 characters, which are each 1 byte long, and turned it into 4 6-bit values that we turned back into characters using our index table.  Lots of steps involved!

What happens when we don't have an even multiple of 3 in our source message?  We need to do some padding to finish out the 24-bit number nicely.  In base64 we use the `=` symbol as the padding character.  Let's assume we only have one character to encode, the letter `M`.

![Base64 padding example](/ycj/images/base64_padding_example.png)

Now we have enough information to do an example.  Let's take the phrase `Hello World!` and base64 encode it.  Here is the algorithm:
 1. Look up the ASCII value for the character in the [ASCII chart](https://en.wikipedia.org/wiki/ASCII) and write down the binary code.
 2. 

<button onclick="showHide('ct1')">Click here to see the answer</button>
<div id="ct1" style="display: none;
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
This is the ciphertext message:<br>
<code class="highlighter-rouge">A nfzx xjzw umryik!</code><br>
Did you get it right?
</div>



Now it is your turn:

1. Write a message that you want to encrypt.
2. Create a keyword you would like to use.
3. Encrypt your message.
4. Pass the message and the keyword to the person with you and see if they can understand it.

Keep doing those steps until you feel like you understand the substitution cipher well.

[Click here to learn more about the Vigenère cipher.](https://en.wikipedia.org/wiki/Vigenère_cipher)

Click the next activity on the left when you are ready to continue.

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
