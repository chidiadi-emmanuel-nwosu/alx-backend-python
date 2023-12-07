#!/usr/bin/env python3
from sys import path

path.append('../')

zoom_array =  __import__('102-type_checking').zoom_array

print(zoom_array.__annotations__)
