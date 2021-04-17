
def pal():
    ori = 0
    n = int(input("Enter The Number: "))
    ori = n
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10

    if ori == rev:
        print(ori, "Number is Palindrome")
    else:
        print(ori, "Number is not Palindrome")


pal()