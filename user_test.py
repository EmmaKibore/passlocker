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

   def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list = []

   def test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save multiple accounts objects to our account_list
    '''  

    self.new_user.save_user()
    test_usert = User("Instagram", "Emma", "0000") # new account 
    test_user.save_account()
    self.assertEqual(len(User.user_list),1)

  def test_save_user(self):
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)

  def delete_user(self):

    '''
    delete_user method deletes a saved user from the user-list
    '''    
    self.new_user.delete_contact() # Deleting a user object
      self.new_user.save_user()
      test_user = User ("Instagram", "Emma", "0000")
      test_user.save_user()

      self.new_user.delete_user()
      self.assertEqual(len(User.user_list),1)

  def test_find_user_by_account(self):
    '''
    checks to see if we can find a user by account and display information
    '''

    self.new_user.save_user()
    test_user = Users("Instagram", "Emma", "0000")
    test_user.save_user()

    found_user = user.find_by_account ("Instagram")

    self.assertEqual(found_user.account,username,password) 

  def test_user_exists(self):
      '''
      test to check if we can return a Boolean if we cannot find user.
      '''

     self.new_user_exists(self):
     test_user = Users("Instagram","Emma","0000")
     test_user.save_user()

     user_exists = Users.user_exists("Instagram")

      self.assertTrue(user_exists)
      
    def test_display_all_user(self):
        '''
        method that returns a list of all users saved
        '''

     self.assertEqual(Users.display_user(),Uesrs.users_list)                

if __name__ == '__main__':
     unittest.main()  
