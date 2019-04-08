from user import User
from credentials import Credentials
import random

# def ca_user(user_name, password):
#     """
#     Function to create a new user
#     """
#     new_user = User(user_name, password)
#     return new_user

def ca_account(account_name, user_name, password):
    """
    Function to create a new  account
    """
    new_account = account(account_name, user_name, password)
    return new_account

def create_user(user):
    '''
    Function to create new user
    '''
    user.create_user()

def add_account(accounts):
    '''
    Function to create new user account
    '''
    account.add_account()

def del_account(name):
    '''
    Function to delete an account
    '''
    Credentials.delete_account(name)

def dis_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_all_accounts()

def find_account(name):
    '''
    Function that finds an account by its account name
    '''
    return Credentials.find_by_account(name)

def main():
    print("Hello welcome to your account.What is your name?")
    user_name = input()

    print(f"Hello{user_name}.What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : ca -  create a new account, da - display accounts, fa - find an account, ex - exit the accounts")

        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("-"*10)

            print("user_name.......")
            user_name =input()

            # save_accounts(create_account(account_name ,user_name,password))
            # print('\n')
            # print(f"New Account {user_name} created")
            # print ('\n')

        elif short_code == 'da':

            if dis_accounts():
                print("Here is a list of all your accounts")
                print('\n')

                for account in display_accounts():
                    print(f"{account.user_name}......{account.password}")

                    print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any accounts")
                    print('\n')

        elif short_code == "fa":
            print("Enter the account you want to search for")

            search_account_name = input()
            if check_existing_accounts(search_account):
                search_account_name = find_account_name()
                print(f"{search_accoun_name.user_name} {search_account_name.password}")
                print('-' * 10)

                print(f"Username.........{search_account_name.user_name}")
                print(f"Password..........{search_account_name.password}")
            else:
                print("That contact does not exist")

        elif short_code == "ex":
            print("Adios ...........")
            break
        else:
            print("I did not get that at all. Please use the short codes")

if __name__ == '__main__':
       main()
