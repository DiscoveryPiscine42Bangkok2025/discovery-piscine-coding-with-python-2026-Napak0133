#!/usr/bin/env python3

a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))

ans = a*b

print(f"{a} x {b} = {ans}")

if ans > 0:
    print("The result is positive.")
elif ans < 0:
    print("The result is negative.")
else: 
    print("The result is positive and negative.")