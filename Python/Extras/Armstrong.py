def arm():
    rev = 0
    a = int(input("Enter The Number: "))
    ori = a
    while a != 0:
        rem = a % 10
        rev = rem * rem * rem + rev
        a //= 10

    if ori == rev:
        print(ori, "Number is Armstrong")
    else:
        print(ori, "Number is not Armstrong")


arm()