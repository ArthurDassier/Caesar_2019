#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct

character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

def find_english_score(input_bytes):
    english_score = []
    for byte in input_bytes.lower():
        actual_score = character_frequencies.get(chr(byte), 0)
        english_score.append(actual_score)
    return sum(english_score)

def xor_on_char(input_bytes, char_value):
    final_sentence = b''
    for index in input_bytes:
        final_sentence += bytes([index ^ char_value])
    return final_sentence

def single_byte_xor(line):
    tab_of_data = []
    for key_value in range(256):
        message = xor_on_char(line, key_value)
        score = find_english_score(message)
        data = {
            'score': score,
            'key': key_value
            }
        tab_of_data.append(data)
    best_score = sorted(tab_of_data, key=lambda x: x['score'], reverse=True)[0]
    return (best_score)

def hamming_distance(str_one, str_two):
    distance = 0

    for x, y in zip(str_one, str_two):
        xored = operator.xor(x, y)
        distance += sum([1 for bits in bin(xored) if bits == '1'])
    return distance

def repeating_key_xor(message_bytes, key):
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes

def first_guess(line):
    tab = []
    for keysize in range(4, 41):
        chunks = [line[i:i+keysize] for i in range(0, len(line), keysize)]
        try:
            chunk_1 = chunks[0]
            chunk_2 = chunks[1]
            distance = hamming_distance(chunk_1, chunk_2)
            result = {
                'key': keysize,
                'distance': (distance / keysize)
            }
            tab.append(result)
        except Exception:
            break
    possible_key_lengths = sorted(tab, key=lambda x: x['distance'])[0]
    max_key_length_poss = possible_key_lengths['key']
    possible_plaintext = []
    key = b''
    for i in range(max_key_length_poss):
        block = b''
        for j in range(i, len(line), max_key_length_poss):
            block += bytes([line[j]])
        key += bytes([single_byte_xor(block)['key']])
        possible_plaintext.append((repeating_key_xor(line, key), key))
    tab_key = max(possible_plaintext, key=lambda x: find_english_score(x[0]))
    print(bytes.hex(tab_key[1]).upper())

def main():
    with open(sys.argv[1], 'r') as file:
        line = file.read()
        line = line.replace(" ", "")
        line = line.replace("\n", "")
    first_guess(bytes.fromhex(line))

if __name__ == "__main__":
    try:
        main()
    except Exception:
      exit(84)
