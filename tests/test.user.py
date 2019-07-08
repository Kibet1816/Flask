import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    """
    Class to test all instances of the user class
    """
    def setUp(self):
        """
        Method that creates an instance of the user class before each test
        """
        self.new_user = User(password = 'barcelona')


    def test_password_setter(self):
        """
        Test method to ascertain pass_secure contains a hashed value
        """
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        """
        Test method to check that the application raises an Attribute error
        """
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        """
        Test method that tests the password verification
        """
        self.assertTrue(self.new_user.verify_password('barcelona'))