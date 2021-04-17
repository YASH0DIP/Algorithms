def fact():
    fact = 1
    i = 1
    n = int(input("Ente the Number"))
    while i <= n:
        fact = fact * i
        i += 1

    print("Factorial of given number is", fact)


fact()
