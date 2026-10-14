n = int(input("Enter a number: "))
if n > 1:
    for i in range(1, n+1):
        if n % i == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")
    print()