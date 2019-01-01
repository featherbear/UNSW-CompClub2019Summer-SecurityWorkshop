#!/bin/python3

# The number of different combinations for a string of length n, is n-1 (+1 for the string itself)

print("-------------------------")
print("       Interleave        ")
print("=========================")
print("1. Encrypt a message     ")
print("2. Decrypt a message     ")
print("-------------------------")


def encrypt(message, rotations):
    result = ""
    for i in range(rotations):
        result += message[i::rotations]
    return result

def decrypt(message, rotations):
    length = len(message)
    result = ""
    steps = [len(message[i::rotations]) for i in range(rotations)]
    j = 0
    for i in range(length):
        result += message[j]
        j += steps[i % rotations]
        if j >= length:
            j += 1
            j -= length
    return result


assert(encrypt(decrypt("5206677", 3), 3) == "5206677")
assert(decrypt(encrypt("5206677", 3), 3) == "5206677")

## There are n combinations

# inputstr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# a = encrypt(inputstr, 5)
#
# i = 1
# old = []
# while True:
#     v = decrypt(a, i)
#     if v in old: break
#     print(i, v)
#     # if v == inputstr:
#     #     break
#     old.append(v)
#     i += 1


while True:
    action = input("Enter an action > ")
    if not action.isdigit(): continue
    action = int(action)

    if action != 1 and action != 2: continue

    message = input("Enter the message: ")
    if len(message) == 0: continue

    shifts = input("Enter the interleave amount: ")
    if not shifts.isdigit(): continue
    shifts = int(shifts)

    if action == 1:
        print("Your encrypted message is:")
        print(encrypt(message, shifts))
    else:
        print("Your decrypted message is:")
        print(decrypt(message, shifts))
    print()


