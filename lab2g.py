#!/usr/bin/env python3
# Author: Iman Kamyabizadeh
# Author ID: 150450229
# Date Created: 2024/5/14

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')
