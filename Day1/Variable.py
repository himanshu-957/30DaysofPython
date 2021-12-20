print("|||Welcome to XYZ bank|||")
exist = input("Do you have a existing accounyt(y/n)?")
balance = 100
if exist == 'n':
    name = input("Enter your name: ")
    mob = input("Enter your mobile no.: ")
    age = input("Enter your age: ")
    print("||Your account has been created and account numer is 0123456789 and pin no. is sent on your mobile no.||")
else:
    account = input("Enter your account number: ")
    dep = input("Do you want to deposit(y) or withdraw(n)??: ")
    pin = int(input("Enter you Pin"))
    if pin == 1234:
        if dep == 'y':
            money = int(input("Enter the amount you want to deposit: "))
            balance = balance + money
            print("Your bank balance is ", end="")
            print(balance)
        else:
            credit = int(input("Enter the amount you want to withdraw: "))
            if credit > balance:
                print("||Sorry! You don't have enough balance||")
            else:
                balance = balance - credit
                print("||You can take your money||")
                print("Your bank balance is ", end="")
                print(balance)
    else:
        print("||Sorry you have entered wrong pin||")
