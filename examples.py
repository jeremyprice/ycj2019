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
