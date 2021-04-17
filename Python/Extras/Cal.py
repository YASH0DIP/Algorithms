def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def gt(a,b):
    if a>b:
        return a
    else:
        return b

def lt(a,b):
    if a<b:
        return b
    else:
        return a

def mod(a,b):
    return a%b

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. GreaterThan")
print("6. LessThan")
print("7. Modulus")

res = int(input("Enter Your Choice: "))
if res==1:
    print(add(a,b))
elif res==2:
    print(sub(a,b))
elif res==3:
    print(mul(a,b))
elif res==4:
    print(div(a,b))
elif res==5:
    print(gt(a,b))
elif res==6:
    print(lt(a,b))
elif res==7:
    print(mod(a,b))


    
