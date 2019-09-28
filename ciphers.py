#!/usr/bin/python3

import string


class cipher(object):
    def encrypt(self, message):
        raise NotImplementedError()

    def decrypt(self, message):
        raise NotImplementedError()


class shift(cipher):
    def encrypt(self, plaintext, distance):
        ciphertext = []
        for letter in plaintext:
            if letter in string.punctuation or letter in string.whitespace:
                ciphertext.append(letter)
                continue
            if letter.islower():
                base = ord('a')
            else:
                base = ord('A')
            cipherletter = (ord(letter) - base + distance) % 26
            cipherletter += base
            ciphertext.append(chr(cipherletter))
        return ''.join(ciphertext)

    def decrypt(self, ciphertext, distance):
        plaintext = []
        for letter in ciphertext:
            if letter in string.punctuation or letter in string.whitespace:
                plaintext.append(letter)
                continue
            if letter.islower():
                base = ord('a')
            else:
                base = ord('A')
            plainletter = (ord(letter) - base - distance) % 26
            plainletter += base
            plaintext.append(chr(plainletter))
        return ''.join(plaintext)
