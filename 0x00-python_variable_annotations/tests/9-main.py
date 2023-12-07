#!/usr/bin/env python3
from sys import path

path.append('../')

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
