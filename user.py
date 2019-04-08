import pyperclip

class User:
    """
    Class that generates new instances of users
    """

    user_list = []
    def __init__(self,account,username,password):
        '''
        the init method helps in defining properties properties of our objects
        '''
        self.username = username
        self.account = account
        self.password = password

        def save_user(self):

            '''
            save_user method saves user objects into user_list
            '''

            User.user_list.append(self)

    
