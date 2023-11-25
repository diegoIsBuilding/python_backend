def signup():
    print('Create a new account')
    #store the user input into username and password
    username = input('Enter new username: ')
    password = input('Enter new password: ')
    #with the open() function - append/create the users.txt file
    #in the user.txt file write the username:password to the file
    #save the file
    with open('users.txt', 'a') as file:
        file.write(f'{username}:{password}')
    
    print('Signup Successful!')
    
def login():
    username = input('Enter Username: ')
    password = input('Enter password: ')
    
    with open('users.txt', 'r') as file:
        for line in file:
            u, p = line.split(':')
            if u == username and p == password:
                print('Login Successful')
                return True
            
    print('Invalid Credentials')
    return False

def main_menu():
    while True:
        choice = input('1: Signup\n2: Login\nChoose (1/2): ')
        if choice == '1':
            signup()
        elif choice == '2':
            if login():
                #Exits the application 
                break
        else:
            print('Invalid Choice')
            
if __name__ == '__main__':
    main_menu()
            