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
