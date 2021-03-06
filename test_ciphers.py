#!/usr/bin/env python3

import ciphers
import unittest
import random
import string


class TestShiftCipher(unittest.TestCase):
    def test_distance3_encrypt(self):
        shift = ciphers.shift()
        plaintext = 'abc'
        expected = 'def'
        ciphertext = shift.encrypt(plaintext, 3)
        self.assertEqual(ciphertext, expected)

    def test_distance3_decrypt(self):
        shift = ciphers.shift()
        ciphertext = 'def'
        expected = 'abc'
        plaintext = shift.decrypt(ciphertext, 3)
        self.assertEqual(plaintext, expected)

    def test_wraparound_encrypt(self):
        shift = ciphers.shift()
        plaintext = 'xyz'
        expected = 'abc'
        ciphertext = shift.encrypt(plaintext, 3)
        self.assertEqual(ciphertext, expected)

    def test_wraparound_decrypt(self):
        shift = ciphers.shift()
        ciphertext = 'abc'
        expected = 'xyz'
        plaintext = shift.decrypt(ciphertext, 3)
        self.assertEqual(plaintext, expected)

    def test_punctuation_encrypt(self):
        shift = ciphers.shift()
        plaintext = 'x,y,z/'
        expected = 'a,b,c/'
        ciphertext = shift.encrypt(plaintext, 3)
        self.assertEqual(ciphertext, expected)

    def test_punctuation_decrypt(self):
        shift = ciphers.shift()
        ciphertext = 'a,b,c/'
        expected = 'x,y,z/'
        plaintext = shift.decrypt(ciphertext, 3)
        self.assertEqual(plaintext, expected)

    def test_whitespace_encrypt(self):
        shift = ciphers.shift()
        plaintext = 'x y z'
        expected = 'a b c'
        ciphertext = shift.encrypt(plaintext, 3)
        self.assertEqual(ciphertext, expected)

    def test_whitespace_decrypt(self):
        shift = ciphers.shift()
        ciphertext = 'a b c'
        expected = 'x y z'
        plaintext = shift.decrypt(ciphertext, 3)
        self.assertEqual(plaintext, expected)


class TestSubstitutionCipher(unittest.TestCase):
    def test_short_encrypt(self):
        subs = ciphers.substitution()
        plaintext = 'abc'
        key = 'xhe' + 23*' '
        expected = 'xhe'
        ciphertext = subs.encrypt(plaintext, key)
        self.assertEqual(ciphertext, expected)

    def test_short_decrypt(self):
        subs = ciphers.substitution()
        ciphertext = 'xhe'
        key = 'xhe' + 23*' '
        expected = 'abc'
        plaintext = subs.decrypt(ciphertext, key)
        self.assertEqual(plaintext, expected)

    def test_full_encrypt(self):
        subs = ciphers.substitution()
        plaintext = 'hello'
        key = 'qagydutpohckbjxsmwvrfizeln'
        expected = 'pdkkx'
        ciphertext = subs.encrypt(plaintext, key)
        self.assertEqual(ciphertext, expected)

    def test_full_decrypt(self):
        subs = ciphers.substitution()
        ciphertext = 'pdkkx'
        key = 'qagydutpohckbjxsmwvrfizeln'
        expected = 'hello'
        plaintext = subs.decrypt(ciphertext, key)
        self.assertEqual(plaintext, expected)

    def test_random_roundtrip(self):
        subs = ciphers.substitution()
        expected = 'This is a secret!'
        for i in range(100):  # run 100 random keys through the round trip
            key = ''.join(random.sample(string.ascii_lowercase, k=len(string.ascii_lowercase)))
            ciphertext = subs.encrypt(expected, key)
            plaintext = subs.decrypt(ciphertext, key)
            self.assertEqual(plaintext, expected)


class TestVigenereCipher(unittest.TestCase):
    def test_wikipedia_encrypt(self):
        v = ciphers.vigenere()
        expected = 'LXFOPVEFRNHR'
        plaintext = 'ATTACKATDAWN'
        keyword = 'LEMON'
        ciphertext = v.encrypt(plaintext, keyword)
        self.assertEqual(ciphertext, expected)

    def test_wikipedia_decrypt(self):
        v = ciphers.vigenere()
        ciphertext = 'LXFOPVEFRNHR'
        expected = 'ATTACKATDAWN'
        keyword = 'LEMON'
        plaintext = v.decrypt(ciphertext, keyword)
        self.assertEqual(plaintext, expected)

    def test_short_encrypt(self):
        v = ciphers.vigenere()
        expected = 'cdspg'
        plaintext = 'apple'
        keyword = 'code'
        ciphertext = v.encrypt(plaintext, keyword)
        self.assertEqual(ciphertext, expected)

    def test_short_decrypt(self):
        v = ciphers.vigenere()
        expected = 'apple'
        ciphertext = 'cdspg'
        keyword = 'code'
        plaintext = v.decrypt(ciphertext, keyword)
        self.assertEqual(plaintext, expected)

    def test_punc_white_encrypt(self):
        v = ciphers.vigenere()
        expected = 'Zincs Ostch!'
        plaintext = 'Hello World!'
        keyword = 'secret'
        ciphertext = v.encrypt(plaintext, keyword)
        self.assertEqual(ciphertext, expected)

    def test_punc_white_decrypt(self):
        v = ciphers.vigenere()
        ciphertext = 'Zincs Ostch!'
        expected = 'Hello World!'
        keyword = 'secret'
        plaintext = v.decrypt(ciphertext, keyword)
        self.assertEqual(plaintext, expected)


class TestBase64Cipher(unittest.TestCase):
    def test_encrypt(self):
        b64 = ciphers.base64()
        plaintext = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
        expected = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="
        ciphertext = b64.encrypt(plaintext)
        self.assertEqual(ciphertext, expected)


if __name__ == '__main__':
    unittest.main()
