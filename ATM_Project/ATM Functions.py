import random

# Customer Data dictionary
cust_data = {}

# Attributes for the new user
new_user_attributes = ['name', 'address', 'phone num', 'govt id', 'amount']

# Function to add a new user
def new_user():
    acc_num = random.randint(10000, 99999)
    while acc_num in cust_data.keys():
        acc_num = random.randint(10000, 99999)  # Ensure account number is unique
    
    # Collecting user details
    new_user_input = []
    for i in new_user_attributes:
        user_input = input(f"Enter {i}: ")
        if i == "amount":
            try:
                new_user_input.append(int(user_input))  # Ensure the amount is an integer
            except ValueError:
                print("Please enter a valid integer for the amount.")
                return
        else:
            new_user_input.append(user_input)

    # Create a dictionary for the new user and add it to cust_data
    a = dict(zip(new_user_attributes, new_user_input))
    cust_data[acc_num] = a
    
    print(f'''
        Your details are added successfully.
        Your account number is {acc_num}
        Please don't lose it.
    ''')

# Function to handle existing user actions
def existing_user():
    accnum = int(input("Please enter your account number: "))
    
    # Ensure correct account number
    while accnum not in cust_data.keys():
        print("Not found. Please enter your correct account number.")
        accnum = int(input("Please enter your account number: "))
    
    # Access account details
    print(f"""
        Welcome, {cust_data[accnum]['name']}!
        Enter 1 to check your balance.
        Enter 2 to withdraw an amount.
        Enter 3 to deposit an amount.
    """)
    
    user_input = int(input())
    
    while user_input not in [1, 2, 3]:
        print("""
            Invalid input!
            Enter 1 to check your balance.
            Enter 2 to withdraw an amount.
            Enter 3 to deposit an amount.
        """)
        user_input = int(input())
    
    if user_input == 1:
        print(f"Your available balance is {cust_data[accnum]['amount']}")
    
    elif user_input == 2:
        withdrawl = int(input("Enter amount to withdraw: "))
        if withdrawl > cust_data[accnum]['amount']:
            print(f"Insufficient balance. Available balance: {cust_data[accnum]['amount']}")
        else:
            cust_data[accnum]['amount'] -= withdrawl
            print(f"Withdrawal successful. Available balance: {cust_data[accnum]['amount']}")
    
    elif user_input == 3:
        deposit = int(input("Enter amount to deposit: "))
        cust_data[accnum]['amount'] += deposit
        print(f"Deposit successful. Available balance: {cust_data[accnum]['amount']}")

# Main Infinite loop
while True:
    print("""
        Welcome to the Horizon Bank!
        Enter 1 if you are a new customer.
        Enter 2 if you are an existing customer.
        Enter 3 to terminate the application.
    """)
    
    user_input = int(input())
    
    while user_input not in [1, 2, 3]:
        print("""
            Invalid input!
            Enter 1 if you are a new customer.
            Enter 2 if you are an existing customer.
            Enter 3 to terminate the application.
        """)
        user_input = int(input())
    
    if user_input == 1:
        new_user()
        print('Thank you for banking with us!')
        break
    elif user_input == 2:
        existing_user()
        print('Thank you for banking with us!')
        break
    else:
        print('Thank you for banking with u')
        break