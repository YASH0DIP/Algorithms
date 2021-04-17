nm = int(input("Enter Number: "))
print("1.Km - Miles")
print("2.Miles - Km")
ops = int(input("Enter Option: "))
if ops == 1:
    miles = (nm * 0.621371)
    print(miles)
else:
    km = (nm / 0.621371)
    print(km)
