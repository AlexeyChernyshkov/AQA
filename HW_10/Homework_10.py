class Bank_Account():
    def __init__(self, name: str, balance: int):
        self._name = name
        self._balance = balance

    def show(self): # Просмотр баланса
        print(f"Owner {self._name} has ${self._balance} on balance")

    def deposit(self, money):   # Депозит на балансу
        self._balance += money
        print(f"Balance: {self._balance}")

    def withdrawal(self, money): # Снятие средств
        if money > self._balance:
            print(f"Not enough money. Can withdrawal only ${self._balance}")
            exit()
        else:
            self._balance -= money
            print(f"Balance: {self._balance}")

    def operation_choice(self): # Выбор операции
        choice = int(input(f"Choose operation:\n"
                           f"1 — Сash withdrawal\n"
                           f"2 — Cash deposit\n"
                           f"3 — No, thanks\n"))
        if choice == 3:
            print("Exit...")
            exit()
        else:
            summ = int(input("Input summ of operation:\n"))
            assert summ >= 0 and type(summ) == int, "Error! Invalid amount value"
        if choice == 1:
            self.withdrawal(summ)
        elif choice == 2:
            self.deposit(summ)
        else:
            print("No operation. Exit...")
            exit()


owner1 = Bank_Account("Ivan", 20000)
owner1.show()
owner1.operation_choice()
