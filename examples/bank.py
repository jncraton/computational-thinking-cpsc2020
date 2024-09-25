balance = 0

def get_number(msg):
    try:
        choice = int(input(msg))
    except ValueError:
        print("That's not a number.")
        return get_number(msg)
    
    return choice

def get_choice():
    print("Welcome to you bank!")
    print("What would you like to do?")
    print("1 Check balance")
    print("2 Deposit")
    print("3 Withdraw")
    
    choice = get_number("Enter you choice")
    
    if choice < 0 or choice > 3:
        print("That's not a valid number.")
        return get_choice()
    
    return choice

def check_balance():
    print("Your balance is:", balance)

def deposit(balance):
    amount = get_number("Enter a deposit amount:")
    
    return balance + amount

def withdraw(balance):
    amount = get_number("Enter a withdraw amount:")
    
    return balance - amount

choice = get_choice()

if choice == 1:
    check_balance()
elif choice == 2:
    balance = deposit(balance)
    check_balance()
elif choice == 3:
    balance = withdraw(balance)
    check_balance()
