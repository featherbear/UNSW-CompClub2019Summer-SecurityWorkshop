#!/bin/python3

print("-------------------------")
print("      Caesar Cipher      ")
print("=========================")
print("1. Encrypt a message     ")
print("2. Decrypt a message     ")
print("-------------------------")

def translate(char, shifts):
    if char.isupper():
        pos = ord(char) - ord('A')
        pos = (pos + shifts) % 26
        return chr(ord('A') + pos)
    elif char.islower():
        pos = ord(char) - ord('a')
        pos = (pos + shifts) % 26
        return chr(ord('a') + pos)
    else:
        return char

def shift(message, shifts):
    return ''.join(translate(char, shifts) for char in message)

assert(shift(shift("5206677", -3), 3) == "5206677")
assert(shift(shift("5206677", 3), -3) == "5206677")

while True:
    action = input("Enter an action > ")
    if not action.isdigit(): continue
    action = int(action)

    if action != 1 and action != 2: continue

    message = input("Enter the message: ")
    if len(message) == 0: continue

    shifts = input("Enter the number of shifts: ")
    if not shifts.isdigit(): continue
    shifts = int(shifts)

    if action == 1:
        print("Your encrypted message is:")
        print(shift(message, shifts))
    else:
        print("Your decrypted message is:")
        print(shift(message, -shifts))
    print()