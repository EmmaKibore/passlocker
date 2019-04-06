class User :
    '''
    Class that generates new instances of user
    '''

    user_list = []
    def __init__ (self, account, password):
        '''
        __init__ method that helps us define properties for our objects
        '''
        self.account = account
        self.username = username
        self.password = password

        user_list = []
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        ''' 

        User.user_list.append(self)
    def delete_user(self)
        User.user_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        for user in cls.user_list:
            if user.account == account:
                return user           