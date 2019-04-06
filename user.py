account_list = [] # Empty accounts list

  def save_account(self):

      '''
      save_account method saves account objects into account_list
      '''

      Account.account_list.append(self)