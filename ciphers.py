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


class substitution(cipher):
    def encrypt(self, plaintext, key):
        t = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                          key.lower() + key.upper())
        return plaintext.translate(t)

    def decrypt(self, ciphertext, key):
        t = str.maketrans(key.lower() + key.upper(),
                          string.ascii_lowercase + string.ascii_uppercase)
        return ciphertext.translate(t)


class vigenere(cipher):
    def _rotate(self, input, distance):
        return input[-distance:] + input[0:-distance]

    def encrypt(self, plaintext, keyword):
        keyword = keyword.lower()
        key = keyword
        while len(keyword) < len(plaintext):
            keyword += key
        ciphertext = []
        for idx, letter in enumerate(plaintext):
            key = keyword[idx]
            shift = -(ord(key) - ord('a'))
            if letter.isupper():
                letter_idx = ord(letter) - ord('A')
                lookup = string.ascii_uppercase
            else:
                letter_idx = ord(letter) - ord('a')
                lookup = string.ascii_lowercase
            cipher = self._rotate(lookup, shift)
            ciphertext.append(cipher[letter_idx])
        return ''.join(ciphertext)

    def decrypt(self, ciphertext, keyword):
        keyword = keyword.lower()
        key = keyword
        while len(keyword) < len(ciphertext):
            keyword += key
        plaintext = []
        for idx, letter in enumerate(ciphertext):
            key = keyword[idx]
            shift = -(ord(key) - ord('a'))
            if letter.isupper():
                lookup = string.ascii_uppercase
            else:
                lookup = string.ascii_lowercase
            cipher = self._rotate(lookup, shift)
            letter_idx = cipher.find(letter)
            plaintext.append(lookup[letter_idx])
        return ''.join(plaintext)
