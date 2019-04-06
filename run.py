def main():
    print("Hello welcome to your account.What is your name?")
      user_name = input()

      print("Hello{user_name}.What would you like to do?")
      print('\n')

      while True:
          print("Use these short codes : cc -  create a new account, dc - display accounts, fc - find an account, ex - exit the accounts")

          short_code = input().lower()

          if short_code == 'ca':
              print("New account")
              print()

              print(user_name.......")

              save_accounts(create_account(account ,user_name,password))
              print('\n')
              print(f"New Account {user_name} created")
              print ('\n')

           elif short_code == 'da':

               if display_accounts():
                   print("Here is a list of all your accounts")
                   print('\n')

                   for account in display_accounts():
                       print(f"{account.account} {account})    
