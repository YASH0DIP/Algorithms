from time import sleep
nm = int(input("Enter Number: "))
print("1.Celsius -> Fahrenheit")
print("2.Fahrenheit -> Celsius")
ops = int(input("Enter the Option: "))
if ops == 1:
    ft = (nm * 1.8) + 32
    print(ft)
else:
    cs = (nm - 32) * (5/9)
    print(cs)
sleep(100)