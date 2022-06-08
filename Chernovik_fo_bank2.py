def ENbank():
    while True:
        a = input("Select an operation:\n""1.Cash replenishment\n""2.Cash withdrawal\n""3. Account balance\n"
                  "4. Operations in the ERIP calculation system:\n""5. Return the card.\n")
        if a == "1":
            money = input("Please insert banknotes into the bill acceptor:\n""1.Continue\n""2.Cancel\n")
            if money == "1":
                print("Balance replenished successfully")
            elif money == "2":
                print("The operation has been cancelled.")
        elif a == "2":
            money = input("Enter withdrawal amount:")
            if money.isdigit():
                summa = input("1.Continue\n""2.Cancel\n")
                if summa == "1":
                    print("Take money from the bill acceptor")
                else:
                    continue
        elif a == "3":
            chek = input("1.Print a receipt\n""2.Display the balance on the screen\n")
            if chek == "1":
                print("Take a check")
            else:
                print("5000\n""BYN")
        elif a == "4":
            print("At the moment, operations in the ERIP payment system are temporarily unavailable. We apologize.")
        elif a == "5":
            print("Take a card")
            break
        elif a not in "12345":
            continue
