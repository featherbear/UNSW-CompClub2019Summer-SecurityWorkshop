# "{0:08b}".format(n)

number = int(input("Enter a decimal: "))

values = []

while number:
    values.append(str(number % 2))
    number = int(number / 2)

print("0b" + "".join(values[::-1]))