---
layout: single
title:  "Cryptography Challenges"
permalink: /challenges.html
---

## Congratulations!

Now that you know the [Shift Cipher](/ycj/shift), the [Substitution Cipher](/ycj/substitution), and the [Vigenère Cipher](/ycj/vigenere) you are ready to try to decode some intercepted communications.  Below are some communications we've intercepted.  The encryption cipher is unknown, as well as any of the cipher parameters.  To succeed at each challenge you will need to determine the encryption cipher, it's parameters, and decode the message.  We believe that all the messages are common phrases or documents, but you'll have to verify our assumptions.  Good luck!

## Challenge no. 1
`Ow lzw Hwghdw gx lzw Mfalwv Klslwk, af Gjvwj lg xgje s egjw hwjxwul Mfagf, wklstdakz Bmklauw, afkmjw vgewklau Ljsfimadalq, hjgnavw xgj lzw ugeegf vwxwfuw, hjgeglw lzw ywfwjsd Owdxsjw, sfv kwumjw lzw Tdwkkafyk gx Datwjlq lg gmjkwdnwk sfv gmj Hgklwjalq, vg gjvsaf sfv wklstdakz lzak Ugfklalmlagf xgj lzw Mfalwv Klslwk gx Sewjaus.
`

<button onclick="showHide('ch1')">Need a hint?</button>
<div id="ch1" style="display: none;
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
It looks like it might be a shift cipher...
</div>

<button onclick="showHide('cs1')">Click here for the solution</button>
<div id="cs1" style="display: none;
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
It is a shift cipher with a distance of <code class="highlighter-rouge">-8</code><br>
Here is the plaintext:<br>
<code class="highlighter-rouge">We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.</code><br>
</div>

## Challenge no. 2
`G yjgmeg ynuciryplc cm cfg Dnje xd cfg Sprrgm Ucyvnq xd Jkgagej, jlf rq rjn Tnnwkjkl hxp ffklf rr brcwbu, qwc Wyvrmp spmct Eqm, rlfrtkbgduc, ukcf ugdnpvh cwb ssucgen hxp jjn.`

<button onclick="showHide('ch2')">Need a hint?</button>
<div id="ch2" style="display: none;
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
This one looks more like a Vigenère cipher...
</div>

<button onclick="showHide('cs2')">Click here for the solution</button>
<div id="cs2" style="display: none;
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
It is a Vigenère cipher with a keyword of <code class="highlighter-rouge">ycj</code><br>
Here is the plaintext:<br>
<code class="highlighter-rouge">I pledge allegiance to the Flag of the United States of America, and to the Republic for which it stands, one Nation under God, indivisible, with liberty and justice for all.</code><br>
</div>

## Challenge no. 3
`Yxdxr qyn Qnzjb csjo; T msnvon jssnotjdgn qx qynn, Qnzjb, xdn bqjqn pdvnr Oxv, xdn jdv tdvtltbthsn.`

<button onclick="showHide('ch3')">Need a hint?</button>
<div id="ch3" style="display: none;
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
This behaves like a substitution cipher...
</div>

<button onclick="showHide('cs3')">Click here for the solution</button>
<div id="cs3" style="display: none;
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
It is a substitution cipher with a key of <code class="highlighter-rouge">jhgvncoytuiskdxmarbqplfzew</code><br>
Here is the plaintext:<br>
<code class="highlighter-rouge">Honor the Texas flag; I pledge allegiance to thee, Texas, one state under God, one and indivisible.</code><br>
</div>

## Challenge no. 4
`Iyedr Myno Tkw zbyfsnoc sxxyfkdsfo, swzkmdpev kxn pkwsvi-pymecon yed yp cmryyv dswo, rkxnc-yx mywzedsxq zbyqbkwc pyb U-12 cdenoxdc kc govv kc dokmrob zbypoccsyxkv nofovyzwoxd nocsqxon dy lbsxq mywzedob cmsoxmo dy ofobi cmryyv kxn ofobi mvkccbyyw`

<button onclick="showHide('ch4')">Need a hint?</button>
<div id="ch4" style="display: none;
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
This one screams shift cipher...
</div>

<button onclick="showHide('cs4')">Click here for the solution</button>
<div id="cs4" style="display: none;
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
It is a shift cipher with a distance of <code class="highlighter-rouge">10</code><br>
Here is the plaintext:<br>
<code class="highlighter-rouge">Youth Code Jam provides innovative, impactful and family-focused out of school time, hands-on computing programs for K-12 students as well as teacher professional development designed to bring computer science to every school and every classroom.</code><br>
</div>

### Challenge no. 5
This one isn't an encrypted phrase, it is a bigger challenge: Can you write some code that will do these encryption and decryption tasks for you?
 - What language would you write it in?
 - Which part would you write first (encryption or decryption)?
 - Which algorithm would you like to tackle?

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
