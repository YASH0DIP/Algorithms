dict = {}
while True:
        print("-------------Birthday's--------------")
        print("1.Show Birthday's")
        print("2.Add Birthday's")
        print("3.Exit")
        choice = int(input("Enter The Choice :"))
        if choice == 1:
            if len (dict.keys()) == 0:
                print("Nothing To Show")
            else:
                name=input("Enter Name To Look For Birthday's :")
                birthday=dict.get(name,"No Data Found")
                print(birthday)
        elif choice == 2:
            name=input("Enter Name :")
            date=input("Enter Birtdate :")
            dict[name]=date
            print("Birthday Added")
        elif choice == 3:
            break
        else:
            print("Choose A Valid Option...")
