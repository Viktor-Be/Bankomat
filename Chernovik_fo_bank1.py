def RUbank():
    while True:
        a = input("Выберите операцию:\n""1.Пополнение наличными\n""2.Снятие наличных\n""3.Остаток на счёте\n"
                  "4.Операции в системе расчёта ЕРИП:\n""5.Вернуть карту.\n")
        if a == "1":
            money = input("Пожалуйста вставьте купюры в купюроприемник:\n""1.Продолжить\n""2.Отмена\n")
            if money == "1":
                print("Баланс успешно пополненю")
            elif money == "2":
                print("Операция отменена.")
        elif a == "2":
            money = input("Введите сумму снятия:")
            if money.isdigit():
                summa = input("1.Продолжить\n""2.Отмена\n")
                if summa == "1":
                    print("Возьмите деньги из купюроприемника")
                else:
                    continue
        elif a == "3":
            chek = input("1.Напечатать чек\n""2.Отоброзить баланс на экране\n")
            if chek == "1":
                print("Возьмите чек")
            else:
                print("5000\n""BYN")
        elif a == "4":
            print("В днный момент операции в системе расёта ЕРИП временно недоступны. Приносим свои извинения.")
        elif a == "5":
            print("Возьмите карту")
            break
        elif a not in "12345":
            continue