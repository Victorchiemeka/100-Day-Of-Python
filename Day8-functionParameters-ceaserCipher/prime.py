def prime_checker(number):
    isPrime = True
    for i in range(2, number - 1):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("This is a prime number")
    else:
        print("This is not a prime number")


n = int(input("Enter a Number: "))
prime_checker(number=n)
