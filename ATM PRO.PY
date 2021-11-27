f = open('Atmdata.txt', 'r')
l = f.readlines()
f.close()

usernames = eval(l[0])
pins = eval(l[1])
balances = eval(l[2])

class Change():
    def __init__(self):
        pass

    def pin_change(self, i):
        temp = 0
        while temp < 3:
            oldpin = int(input("Enter the Current Pin"))
            if oldpin == pins[i]:
                    newpin = int(input("Enter the New Pin"))
                    confirmpin = int(input("Confirm your Pin"))
                    if newpin == confirmpin:
                        print("Your Pin Succesfully changed")
                        f = open('Atmdata.txt', 'w')
                        pins[i] = confirmpin
                        f.write("%s\n%s\n%s" %(usernames, pins, balances))
                        f.close()
                    else:
                        print("Enter your pin correctly")
                    break
            else:
                print("Try Again.............")
            temp = temp + 1
            if temp == 3:
                print("3 Wrong Input, Your card is blocked for 24 hrs.")

class Statement():
    def __init__(self):
        pass

    def balance_check(self, i):
        bal = balances[i]
        print("Your balance is : ", bal)

class Debit:
    def __init__(self):
        pass

    def withdraw(self, i):
        bal1 = balances[i]
        amt = int(input("Enter the Amount to withdraw"))
        if amt % 100 == 0:
            if amt > bal1:
                print("Insufficient Balance")
            else:
                print("Collect your Cash : ", amt)
        else:
            print("Denomination 100 only available")
        choice2 = int(input("Enter : 1 for Display Balance or Enter : 2 for EXIT"))
        if choice2 == 1:
            bal1 = bal1 - amt
            f = open('Atmdata.txt', 'w')
            balances[i] = bal1
            f.write("%s\n%s\n%s" %(usernames, pins, balances))
            f.close()
            print("Your Balance is : ", bal1)
        else:
            exit()

class Credit:
    def __init__(self):
        pass

    def deposit(self, i):
        bal2 = balances[i]
        dep = int(input("Tell ME!!!!!! How Much Money You Want to DEPOSIT: "))
        print("Your Deposited Money is : ", dep)
        choice3 = int(input("Enter : 1 for Display Balance or Enter : 2 for EXIT"))
        if choice3 == 1:
            bal2 = bal2 + dep
            f = open('Atmdata.txt', 'w')
            balances[i] = bal2
            f.write("%s\n%s\n%s" %(usernames, pins, balances))
            f.close()
            print("Your Balance is : ",bal2)
        else:
            exit()

class Main_Menu(Statement, Debit, Credit, Change):
    def __init__(self):
        Statement.__init__(self)
        Debit.__init__(self)
        Credit.__init__(self)
        Change.__init__(self)
        

    def continue_transaction(self, i):
        n = input("Do you want to continue this transaction? \"y/n\" : ")
        if n == 'y':
            self.show_menu(i)
        elif n == 'n':
            exit()
        else:
            self.continue_transaction(i)

    def show_menu(self, i):
        print("Hello Mr.", usernames[i])
        print(" ---------------------------")
        print("|        Main Menu                   *")
        print("| Enter 1 for Balance Check     *")
        print("| Enter 2 for Withdraw             *")
        print("| Enter 3 for Deposit               *")
        print("| Enter 4 for Pin Change          *")
        print("| Enter 5 for Exit                    *")
        print(" ---------------------------")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            self.balance_check(i)
        elif choice == 2:
            self.withdraw(i)
        elif choice == 3:
            self.deposit(i)
        elif choice == 4:
            self.pin_change(i)
        elif choice == 5:
            exit()
        else:
            self.show_menu(i)

        self.continue_transaction(i)


class Login(Main_Menu):
    def __init__(self):
        Main_Menu.__init__(self)

    def verify_username(self):
        print("-----------------------------------------------")
        print("                     Welcome to SBI ATM                         ")
        print("-----------------------------------------------")  
        username = input("Enter the Username : ")
        if username in usernames:
            index_no = usernames.index(username)
            print("Username exists...")
            self.verify_pin(index_no)
        else:
            print("Wrong Username, Try Again...")
            exit()

    def verify_pin(self, i):
        c = 0
        while c < 3:
            pin = int(input("Enter the PIN : "))
            if pin == pins[i]:
                print("Login Successfull...")
                self.show_menu(i)
                break
            else:
                print("Wrong Pin, Try Again...")
            c = c + 1
        if c == 3:
            print("3 Wrong Input, Your card is blocked for 24 hrs.")
            print("---------------------------------------")
            print("                 YOU ARE HACKED                   ")
            print("---------------------------------------")
            

o = Login()
o.verify_username()
