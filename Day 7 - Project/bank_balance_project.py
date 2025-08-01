balance = float(input("Enter your balance: "))

while True:
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice(1 to 4) :"))

    if choice == 1:
        print("You balance is:", balance)
    elif choice == 2:
        deposite = float(input("Enter your deposite amount: "))
        balance += deposite
        print("Amount Deposited Successfully...Thank you!!")
        print("After Deposite Balance is: ", balance)
    elif choice == 3:
        withdraw = float(input("Enter your withdraw amount: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Amount Withdraw Successfully...Thank you!!")
            print("After Withdrawal your balance is: ", balance)
        else:
            print("Your balance is inefficient, you cannot withdraw")
    elif choice == 4:
        print("Exiting. Thank you for using the ATM.")
    else:
        print("Thank you for visiting ATM......")