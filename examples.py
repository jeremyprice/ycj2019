#!/usr/bin/env python3

import ciphers
import string

print('***** shift cipher page *****')
plain = 'Really important message contained herein'
shift = ciphers.shift()
print('Shift by -3: {} | {}'.format(plain, shift.encrypt(plain, -3)))

plain = 'test message'
shift = ciphers.shift()
print('Shift by 2: {} | {}'.format(plain, shift.encrypt(plain, 2)))

plain = "This message isn't negative"
shift = ciphers.shift()
print('Shift by -5: {} | {}'.format(plain, shift.encrypt(plain, -5)))

plain = "Hello World!"
shift = ciphers.shift()
print('Shift by 7: {} | {}'.format(plain, shift.encrypt(plain, 7)))

plain = "Goodbye World?"
shift = ciphers.shift()
print('Shift by -4: {} | {}'.format(plain, shift.encrypt(plain, -4)))

print('***** substitution cipher page *****')
plain = string.ascii_lowercase
shift = ciphers.shift()
print('Shift by 6: {} | {}'.format(plain, shift.encrypt(plain, 6)))

key = 'qagydutpohckbjxsmwvrfizeln'
plain = "It's the best day ever!"
subs = ciphers.substitution()
print('Substitution: {} | {}'.format(plain, subs.encrypt(plain, key)))

key = 'qagydutpohckbjxsmwvrfizeln'
plain = "Thanks for decrypting this"
subs = ciphers.substitution()
print('Substitution: {} | {}'.format(plain, subs.encrypt(plain, key)))

keyword = 'secret'
plain = 'I love this cipher!'
v = ciphers.vigenere()
print('Vigenère: {} | {}'.format(plain, v.encrypt(plain, keyword)))

keyword = 'youthcodejam'
plain = "I hope I don't run out of time"
v = ciphers.vigenere()
print('Vigenère: {} | {}'.format(plain, v.encrypt(plain, keyword)))

print('***** Challenges *****')
plain = 'We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.'
shift = ciphers.shift()
print('Shift by -8: {} | {}'.format(plain, shift.encrypt(plain, -8)))

plain = 'I pledge allegiance to the Flag of the United States of America, and to the Republic for which it stands, one Nation under God, indivisible, with liberty and justice for all.'
keyword = 'ycj'
v = ciphers.vigenere()
print('Vigenère with key "ycj": {} | {}'.format(plain, v.encrypt(plain, keyword)))

plain = 'Honor the Texas flag; I pledge allegiance to thee, Texas, one state under God, one and indivisible.'
key = 'jhgvncoytuiskdxmarbqplfzew'
subs = ciphers.substitution()
print('Substitution key = "jhgvncoytuiskdxmarbqplfzew": {} | {}'.format(plain, subs.encrypt(plain, key)))

plain = 'Youth Code Jam provides innovative, impactful and family-focused out of school time, hands-on computing programs for K-12 students as well as teacher professional development designed to bring computer science to every school and every classroom.'
shift = ciphers.shift()
print('Shift by 10: {} | {}'.format(plain, shift.encrypt(plain, 10)))
