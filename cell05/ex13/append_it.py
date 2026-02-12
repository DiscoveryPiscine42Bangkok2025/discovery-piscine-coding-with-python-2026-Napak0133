#!/usr/bin/env python3

import sys

param = sys.argv[1:] 

if len(param) == 0: 
    print("none")
else:
    for x in param: 
        if not x.endswith("ism"): 
            print(x+ "ism") 
