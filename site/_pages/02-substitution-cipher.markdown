---
layout: single
title:  "Substitution Cipher"
permalink: /substitution
---

Now that you know the shift cipher, let's talk about it's family.  The shift cipher is one form of a substitution cipher.  In a basic substitution cipher we substitute on letter for another letter.  In the shift cipher, we create the key by shifting all the letters by a constant amount.  For instance, here is the key for a shift cipher with a distance of 6:
```
abcdefghijklmnopqrstuvwxyz
ghijklmnopqrstuvwxyzabcdef
```

With a shift cipher it is easy to break the encryption if you figure out a few letters because you can see the pattern that they are shifted by a constant value.  To make our encryption a little stronger we can implement a more generic substitution cipher.  Instead of shifting by a constant amount we could choose a key where each letter corresponded to a random ciphertext letter.  For instance, let's use this key to encrypt our message:
```
abcdefghijklmnopqrstuvwxyz
qagydutpohckbjxsmwvrfizeln
```

Here is what our plaintext and ciphertext would look like:
```
It's the best day ever!
Or'v rpd advr yql didw!
```

Now it is your turn.  Here is the ciphertext, decrypt it using the key listed above.
```
Rpqjcv uxw ydgwlsrojt rpov
```

<button onclick="showHide('pt1')">Click here to see the answer</button>
<div id="pt1" style="display: none;
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
<code class="highlighter-rouge">Thanks for decrypting this</code><br>
Did you get it right?
</div>

Now it is your turn:

1. Write a message that you want to encrypt.
2. Create a key you would like to use.  **Make sure each letter is used only once!**
3. Encrypt your message.
4. Pass it to the person with you and see if they can understand it.

Keep doing those steps until you feel like you understand the substitution cipher well.

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
