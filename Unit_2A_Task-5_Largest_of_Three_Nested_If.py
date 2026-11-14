a = int(input("Enter a first num:"))
b = int(input("Enter a second num:"))
c = int(input("Enter third num:"))
if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c
        print(f"largest{largest} is (amount{a},{b},{c}):")
