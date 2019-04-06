import unittest 
from user import User # importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

 def setUp(self):
    '''
    set up method to run before each test cases.
    '''
    self.new_user = User("Instagram", "Emma", "0000") # create user object

 def test_init(self):
     '''
     test_init case to test if the object is initialized correctly
     '''

     self.assertEqual(self.new_user.account,"Instagram")
     self.assertEqual(self.new_user.username,"Emma")
     self.assertEqual(self.new_user.password,"0000")

#  def tearDown(self):
#     '''
#     tearDown method that does clean up after each test case has run.
#     '''
#     User.user_list = []

#  def test_save_multiple_user(self):
#     '''
#     test_save_multiple_user to check if we can save multiple accounts objects to our account_list
#     '''  

#     self.new_user.save_user()
#     test_usert = User("Instagram", "Emma", "0000") # new account 
#     test_user.save_account()
#     self.assertEqual(len(User.user_list),1)

# def test_save_user(self):
#     self.new_user.save_user()
#     self.assertEqual(len(User.user_list),1)

# def delete_user(self):

#     '''
#     delete_user method deletes a saved user from the user-list
#     '''    
#     self.new_user.delete_contact() # Deleting a user object
# if __name__ == '__main__':
#     unittest.main()  
