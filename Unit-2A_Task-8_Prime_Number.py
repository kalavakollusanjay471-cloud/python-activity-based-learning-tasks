


n = int(input("Enter a number between 1 and 100: "))

if n <= 1:
    print(n, "is not a Prime Number")
else:
    count = 0

    for i in range(2, n):
        if n % i == 0:
            count = count + 1
            break

    if count == 0:
        print(n, "is a Prime Number")
    else:
        print(n, "is not a Prime Number")
