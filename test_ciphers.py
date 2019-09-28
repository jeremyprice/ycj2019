#!/usr/bin/env python3

import ciphers
import unittest


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


if __name__ == '__main__':
    unittest.main()
