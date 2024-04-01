import json
class Bank:
    def __init__(self):
        self.employees = {}
        self.accounts = {}
        self.load_data()

    def load_data(self):
        try:
            with open("employees.txt", "r") as file:
                self.employees = json.load(file)
        except FileNotFoundError:
            self.employees = {}

        try:
            with open("accounts.txt", "r") as file:
                self.accounts = json.load(file)
        except FileNotFoundError:
            self.accounts = {}

    def save_data(self):
        with open("employees.txt", "w") as file:
            json.dump(self.employees, file)

        with open("accounts.txt", "w") as file:
            json.dump(self.accounts, file)
    def admin_portal(self):
        print("\nWelcome to Admin Portal")
        password = input("Enter admin password: ")
        if password == "admin123":  # Hardcoded admin password for demonstration
            print("Admin login successful.")
            while True:
                print("\n1. Create Employee Account")
                print("2. Create Customer Account")
                print("3. Access Employee Accounts")
                print("4. Access Customer Accounts")
                print("5. Display All Employees")
                print("6. Display All Customers")
                print("7. Exit")
                option = input("Select an option: ")

                if option == "1":
                    self.create_employee_account()
                elif option == "2":
                    self.create_customer_account()
                elif option == "3":
                    self.access_employee_accounts()
                elif option == "4":
                    self.access_customer_accounts()
                elif option == "5":
                    self.display_employees()
                elif option == "6":
                    self.display_customers()
                elif option == "7":
                    print("Exiting admin portal...")
                    break
                else:
                    print("Invalid option. Please try again.")
                    print("\n*********************************")
                    print("*********************************")
        else:
            print("Incorrect password.")

    def create_employee_account(self):
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter employee salary: "))
        password = input("Enter employee password: ")
        if emp_id not in self.employees:
            self.employees[emp_id] = {'name': name, 'salary': salary, 'password': password}
            self.save_data()
            print("Employee account created successfully.")
        else:
            print("Employee ID already exists.")

    def create_customer_account(self):
        name = input("Enter customer name: ")
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        balance = float(input("Enter initial balance: "))
        if account_number not in self.accounts:
            self.accounts[account_number] = {'name': name, 'password': password, 'balance': balance}
            self.save_data()
            print("Customer account created successfully.")
        else:
            print("Account number already exists.")

    def access_employee_accounts(self):
        emp_id = input("Enter employee ID: ")
        if emp_id in self.employees:
            print(f"\nEmployee Details:")
            print(f"ID: {emp_id}, Name: {self.employees[emp_id]['name']}, Salary: {self.employees[emp_id]['salary']}")
        else:
            print("Employee not found.")

    def access_customer_accounts(self):
        while True:
            account_number = input("Enter account number: ")
            if account_number in self.accounts:
                print(f"\nCustomer Details:")
                print(f"Account Number: {account_number}, Name: {self.accounts[account_number]['name']}, Balance: {self.accounts[account_number]['balance']}")
                break
            else:
                print("Customer account not found. Please try again.")


    def display_employees(self):
        print("\nAll Employees:")
        for emp_id, emp_data in self.employees.items():
            print(f"ID: {emp_id}, Name: {emp_data['name']}, Salary: {emp_data['salary']}")

    def display_customers(self):
        print("\nAll Customers:")
        for acc_num, acc_data in self.accounts.items():
            print(f"Account Number: {acc_num}, Name: {acc_data['name']}, Balance: {acc_data['balance']}")


    def customer_portal(self):
        while True:
            print("\n")
            print("============================================================================")
            print("==================Welcome to the Customer Information section===============")
            print("============================================================================")
            print("\n")
            account_number = input("Enter account number: ")
            password = input("Enter password: ")

            if account_number in self.accounts and self.accounts[account_number]['password'] == password:
                print("\n")
                print("^^^^^^^^^^^^^^^^^^Please make your choice^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("\n")
                while True:
                    print("Select 1: To View Account Details")
                    print("\n")
                    print("Select 2: To Withdraw Cash")
                    print("\n")
                    print("Select 4: To Deposit Money")
                    print("\n")
                    print("Select 4: To Transfer Money")
                    print("\n")
                    print("Select 5: To Exit")
                    print("\n")
                    option = input("Kindly select your choice : ")

                    if option == "1":
                        self.account_details(account_number)
                    elif option == "2":
                        self.withdraw(account_number)
                    elif option == "3":
                        self.deposit(account_number)
                    elif option == "4":
                        self.transfer(account_number)
                    elif option == "5":
                        print("---------EX---------")
                        print("---------IT---------")
                        print("---------IN---------")
                        print("---------G----------")
                        print("\n")
                        print("-----------------------------------")
                        print("!!        THANKS FOR VISITING    !!")
                        print("-----------------------------------")
                        return
                    else:
                        print("Invalid option. Please try again.")
                        print("\n*********************************")
                        print("*********************************")

            else:
                print("Invalid account number or password. Please try again.")

    def account_details(self, account_number):
        account = self.accounts[account_number]
        print(f"Account holder name: {account['name']}")
        print(f"Account number: {account['account_number']}")
        print(f"Account balance: {account['balance']}")

    def deposit(self, account_number):
        amount = float(input("Enter amount to deposit: "))
        self.accounts[account_number]['balance'] += amount
        print(f"Amount of {amount} deposited. Current Balance: {self.accounts[account_number]['balance']}")

    def withdraw(self, account_number):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.accounts[account_number]['balance']:
            print("Insufficient Balance.")
        else:
            self.accounts[account_number]['balance'] -= amount
            print(f"Withdrew {amount}. Current Balance: {self.accounts[account_number]['balance']}")

    def transfer(self, account_number):
        while True:
            recipient_account_number = input("Enter recipient's account number: ")
            if recipient_account_number in self.accounts:
                recipient = self.accounts[recipient_account_number]
                amount = float(input("Enter amount to transfer: "))
                if amount > self.accounts[account_number]['balance']:
                    print("Insufficient Balance.")
                else:
                    self.accounts[account_number]['balance'] -= amount
                    recipient['balance'] += amount
                    print(f"Transferred {amount} to {recipient['name']}. Your Current Balance: {self.accounts[account_number]['balance']}")
                break
            else:
                print("Invalid recipient account number. No record found. Please try again.")
    
    def employee_portal(self):
        print("\n")
        print("****************************************************************************")
        print("******************Welcome to the Employees portal***************************")
        print("****************************************************************************")
        print("\n")
        emp_id = input("Enter employee ID: ")
        password = input("Enter password: ")
        if emp_id in self.employees and self.employees[emp_id]['password'] == password:
            print("\nEmployee login successful.")
            print("\n!!!!!!!!!WELCOME!!!!!!!!!!!!")
            while True:
                print("\n")
                print("Press Option: 1: ")
                print("For Viewing your Own Details")
                print("\n")
                print("Press Option 2: ")
                print("To Change Password")
                print("\n")
                print("Press Option 3: ")
                print("For Creating Customer Account")
                print("\n")
                print("Press Option 4: ")
                print("For Accessing Customer Account")
                print("\n")
                print("Press Option 5: ")
                print("To EXIT")
                print("\n")                
                option = input("Your Desired Option Is : ")

                if option == "1":
                    self.view_own_details(emp_id)
                elif option == "2":
                    self.change_employee_password(emp_id)
                elif option == "3":
                    self.create_customer_account()
                elif option == "4":
                    self.access_customer_accounts()
                elif option == "5":
                    print("Exiting employee portal")
                    print("!!!-------------------------------!!!")
                    print("!!!        SEE YOU                !!!")
                    print("!!!          SOON                 !!!")
                    print("!!!-------------------------------!!!")
                    break
                else:
                    print("Invalid Option. Please Select the Right Option.")

        else:
            print("Invalid employee ID or password.")

    def view_own_details(self, emp_id):
        print("\nYour Details:")
        print(f"ID: {emp_id}, Name: {self.employees[emp_id]['name']}, Salary: {self.employees[emp_id]['salary']}")

    def change_employee_password(self, emp_id):
        new_password = input("Enter new password: ")
        self.employees[emp_id]['password'] = new_password
        self.save_data()
        print("Password changed successfully.")

        print("\nCustomer Accounts:")
        acc_num = input("Enter account number: ")
        if acc_num in self.accounts:
            print(f"Account Number: {acc_num}, Name: {self.accounts[acc_num]['name']}, Balance: {self.accounts[acc_num]['balance']}")
        else:
            print("Account not found.")
# Main function
class Employee: 
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
   
class Customer:
    def __init__(self, name, account_number, password, balance=0):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = balance
    


def main():
    bank = Bank()
    bank.load_data()

    print()
    print("--------------------------------------------------------------------------------")
    print("-------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-----------")
    print("-------------------------!!Welcome to--(KNOWLEDGE STREAMS)---Bank!!!!-----------")
    print("-------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-----------")
    print("--------------------------------------------------------------------------------")
    print("\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<Please Select from the options>>>>>>>>>>>>>>>>>>>>>>>>>")

    while True:
        print("\n")
        print("Press Option: 1: ")
        print("For accessing Admin portal")
        print("\n")
        print("Press Option 2: ")
        print("To sign in to the employee portal")
        print("\n")
        print("Press Option 3: ")
        print("For accessing Customer Accounts Details")
        print("\n")
        print("Press Option 4: ")
        print("To EXIT")
        print("\n")
        option = input("Your desired option is : ")

        if option == "1":
            bank.admin_portal()
        elif option == "2":
            
            bank.employee_portal()
        elif option == "3":
        
            bank.customer_portal()
        elif option == "4":
            print("@@@@@@@@ Exiting @@@@@@@@@@@@@@@")
            break
        else:
             print("Invalid option. Please try again.")
             print("\n*********************************")
             print("*********************************")



if __name__ == "__main__":
    main()