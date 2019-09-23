#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct

# def get_english_score(input_bytes):
#     """Compares each input byte to a character frequency 
#     chart and returns the score of a message based on the
#     relative frequency the characters occur in the English
#     language
#     """
#     character_frequencies = {
#         'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
#         'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
#         'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
#         'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
#         'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
#         'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
#         'y': .01974, 'z': .00074, ' ': .13000
#     }
#     return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


# def single_char_xor(input_bytes, char_value):
#     """Returns the result of each byte being XOR'd with a single value.
#     """
#     output_bytes = b''
#     for byte in input_bytes:
#         output_bytes += bytes([byte ^ char_value])
#     return output_bytes

# def main():
#     hexstring = '0430272762112D243635233027786204302727262D2F62232C2662012D2D32273023362B2D2C'
#     ciphertext = binascii.unhexlify(hexstring)
#     potential_messages = []
#     for key_value in range(255):
#         message = single_char_xor(ciphertext, key_value)
#         score = get_english_score(message)
#         data = {
#             'message': message,
#             'score': score,
#             'key': key_value
#             }
#         potential_messages.append(data)
#     best_score = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
#     for item in best_score:
#         print("{}: {}".format(item.title(), best_score[item]))

if __name__ == '__main__':
    main()

# def main():
#     with open(sys.argv[1], 'r') as file:
#         # sys.stdout.write(file.readline())
#         test = binascii.unhexlify(file.readline())
#         print(test)
#         strings = (''.join(chr(num ^ key) for num in test) for key in range(256))
#         result = max(strings, key=lambda s: s.count(' '))
#         print(result)

# if __name__ == "__main__":
#     try:
#         main()
#     except Exception:
#         exit(84)