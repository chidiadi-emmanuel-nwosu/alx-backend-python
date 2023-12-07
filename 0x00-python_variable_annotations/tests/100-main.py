#!/usr/bin/env python3
from sys import path

path.append('../')

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)
