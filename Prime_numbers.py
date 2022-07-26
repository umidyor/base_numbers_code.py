x = int(input("Enter a number>>> "))
r = list(range(2, x))
for i in r:
    if x % i == 0:
        print("This is not a prime number!")
        break
    else:
        print("This is a prime number!")