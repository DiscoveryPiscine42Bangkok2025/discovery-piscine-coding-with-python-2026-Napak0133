#!/usr/bin/env python3

import sys

param = sys.argv[1:]

if len(param) == 0:
    print("none")
else:
    print("parameters:", len(param))

    for x in param:
        print(x + ":", len(x))
