class add():
    def __init__(self):
        print("Addition")
    def __add__(self, a, b):
        s = a + b
        print(s)
        return s
ob = add()
ob = add.__add__(add, 10, 5)