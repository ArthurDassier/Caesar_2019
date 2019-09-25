#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct
import base64

from Crypto.Cipher import AES


def unpad(padded):
    padded = padded.decode('utf-8')
    offset = ord(padded[-1])
    return padded[:-offset]


def padding(bytes_block, lenght):

    if len(bytes_block) < lenght:
        to_pad = lenght - len(bytes_block)
        for i in range(to_pad):
            bytes_block += chr(to_pad).encode()

    return (bytes_block)


def main():
    with open(sys.argv[1], 'r') as file:
        key = file.readline()
        key = key.replace(" ", "")
        key = key.replace("\n", "")
        ciphertext = file.read()
        ciphertext = ciphertext.replace(" ", "")
        ciphertext = ciphertext.replace("\n", "")
        ciphertext = base64.b64decode(ciphertext)
        aestext = AES.new(bytes.fromhex(key), AES.MODE_ECB)
        decrypted = aestext.decrypt(ciphertext)
        print(unpad(base64.b64encode(decrypted)))


if __name__ == "__main__":
    #try:
        main()
    #except Exception:
        #exit(84)