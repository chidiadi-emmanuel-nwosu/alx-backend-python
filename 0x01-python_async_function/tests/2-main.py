#!/usr/bin/env python3
from sys import path

path.append('../')
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
