#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct
import base64


def main():
    with open(sys.argv[1], 'r') as file:
        line = file.read()
        line = line.replace(" ", "")
        line = line.splitlines()
        print (line)
       # line = base64.b64decode(line)



if __name__ == "__main__":
    #try:
        main()
    #except Exception:
     #   exit(84)