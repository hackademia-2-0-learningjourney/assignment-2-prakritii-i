import json

# Function to load user data from the JSON file
def get_user_data():
    try:
        with open('login.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Function to save user data to the JSON file
def save_user_data(data):
    with open('login.json', 'w') as f:
        json.dump(data, f, indent=4)

# handle signup
def sign_up():
    user_data = get_user_data()

    u_name = input('Enter username: ')
    pw = input('Enter password: ')
    ph_no = input('Enter Phone Number: ')

    if u_name in user_data:
        print('Username already exists!')
    else:
        user_data[u_name] = {'password': pw, 'mobile_number': ph_no}
        save_user_data(user_data)
        print('Sign-up successful!')

# handle user signin
def sign_in():
    user_data = get_user_data()

    username = input('Enter username: ')
    password = input('Enter password: ')

    if username in user_data and user_data[username]['password'] == password:
        print(f'Welcome, {username}! Your number is {user_data[username]["mobile_number"]}')
    else:
        print('Incorrect credentials.')

# Main function to drive the program
def main():
    while True:
        print('\n1. Sign up')
        print('2. Sign in')
        choice = input('Choose an option (1 or 2): ')

        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        else:
            print('Invalid choice. Exiting the program.')
            break

        # still wanna continue?
        continue_choice = input('Do you want to perform another action? (yes/no): ').strip().lower()
        if continue_choice != 'yes':
            print('Exiting the program. Goodbye!')
            break

if __name__ == "__main__":
    main()