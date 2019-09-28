#!/usr/bin/env python3

import ciphers

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
