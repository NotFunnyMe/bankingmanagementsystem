import os

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    balance = 0.0
    with open("usersreg.txt","a") as file:
        file.write(f"{username},{password},{balance}\n")
    print("You have successfully registered")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("usersreg.txt","r") as file:
        for line in file:
            storedusername, storedpassword, storedbalance = line.strip().split(",")
            if username == storedusername and password == storedpassword:
                print("You have successfully logged in")
                return True
        print("Invalid username or password")
        return False
            

            
def banking_system(balance):
    while True:
        print("Welcome to the banking system")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            balance = deposit(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            break
        else:
            print("Invalid choice")
    return balance


def deposit(balance):
    deposit_amount = float(input("Enter the amount you want to deposit: "))
    balance += deposit_amount
    print(f"Your current balance is {balance}")
    return balance

def withdraw(balance):
    withdraw_amount = float(input("Enter the amount you want to withdraw: "))
    if withdraw_amount > balance:
        print("Insufficient funds")
    else:
        balance -= withdraw_amount
        print(f"Your current balance is {balance}")
    return balance

def check_balance(balance):
    print(f"Your current balance is {balance}")

def main():
    print("Welcome to the login page")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        if login():
            banking_system(0.0)
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()