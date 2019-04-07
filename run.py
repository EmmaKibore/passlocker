def main():
    print("Hello welcome to your account.What is your name?")
    user_name = input()

    print("Hello{user_name}.What would you like to do?")
    print('\n')

    while True:
          print("Use these short codes : ca -  create a new account, da - display accounts, fa - find an account, ex - exit the accounts")

          short_code = input().lower()

          if short_code == 'ca':
              print("New account")
              print()

              print("user_name.......")

              save_accounts(create_account(account ,user_name,password))
              print('\n')
              print(f"New Account {user_name} created")
              print ('\n')

          elif short_code == 'da':

               if display_accounts():
                   print("Here is a list of all your accounts")
                   print('\n')

                   for account in display_accounts():
                       print(f"{account.username}......{account.password}")

                       print('\n')
    else:
                  print('\n')
                  print("You dont seem to have any accounts")
                  print('\n')

          elif short_code == 'fa':
             print("Enter the account you want to search for")

             search_account = input()
             if check_existing_accounts(search_account):
                 search_account = find_account()
                 print(f"{search_account.user_name} {search_account.password}")
                 print('-' * 20)

                 print(f"Username.........{search_account.user_name}")
                 print(f"Password..........{search_account.password}")
             else:
                 print("That contact does not exist")

         elif short_code == "ex":
                print("Bye ...........")
                break
             else:
                 print("I did not get that at all. Please use the short codes")

if __name__ == '__main__':
    main()                                                 


