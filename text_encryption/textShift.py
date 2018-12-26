#!/bin/python3

print("-------------------------")
print("       Text Shift        ")
print("=========================")
print("1. Encrypt a message     ")
print("2. Decrypt a message     ")
print("-------------------------")


def shift(message, rotations):
    length = len(message)
    return message[rotations % length:] + message[:rotations % length]

assert(shift(shift("5206677", -3), 3) == "5206677")
assert(shift(shift("5206677", 3), -3) == "5206677")

while True:
    action = input("Enter an action > ")
    if not action.isdigit(): continue
    action = int(action)

    if action != 1 and action != 2: continue

    message = input("Enter the message: ")
    if len(message) == 0: continue

    key = input("Enter the key: ")
    if not key.isdigit(): continue
    key = int(key)

    if action == 1:
        print("Your encrypted message is:")
        print(shift(message, -key))
    else:
        print("Your decrypted message is:")
        print(shift(message, key))
    print()