import unittest
from ast import match_case
from ssl import _PasswordType
from interface import User
from interface import credentials

class TestClass(unittest.TestCase):
     def __init__(self):
        self.new_user =User('Moglie02','newpassword1234')
        
        def create_key(self):
             self.assertEqual = (self.new_user.username,'Moglie02')
             self.assertEqual = (self.new_user.password,'newpassword1234')
             
             def save_user_file(self):
                 self.save_user_file =()
                 self.assertEqual = (len(User.user_list),1)

             class TestCredentials(unittest.TestCase):
                 def setUp(self):
                     """
                     Method that runs before each individual credentials test methods run.
                     """
                     def test_init(self):
                         self.assertEqual(self.new_credential.account,'Gmail')
                         self.assertEqual(self.new_credential.userName,'Owiti_Charles')
                         self.assertEqual(self.new_credential.password,'yx5Gij43')
                         
                     def save_credential_test(self):
                         self.new_credential.save_details()
                         self.assertEqual(len(credentials.credentials_list),1)
                         def tearDown(self):
                             
                             credentials.credentials_list = []
                             def test_save_many_accounts(self):
                                 self.new_credential.save_details()
                                 test_credential = credentials("Twitter","moglieish","AbCdEfGh")
                                 test_credential.save_details()
                                 self.assertEqual(len(credentials.credentials_list),2)
                                 def test_delete_credential(self):
                                     self.new_credential.save_details()
                                     test_credential = credentials("Twitter","moglieish","AbCdEfGh")
                                     test_credential.save_details()
                                     
                                     self.new_credential.delete_credentials()
                                     self.assertEqual(len(credentials.credentials_list),1)
                                     def test_find_credentialr(self):
                                         self.new_credential.save_details()
                                         
                                         test_credential = credentials("Twitter","moglieish","AbCdEfGh")
                                         test_credential.save_details()
                                         the_credential = credentials.find_credential("Twitter")
                                         self.assertEqual(the_credential.account,test_credential.account)
                                         def test_credential_exist(self):
                                             self.new_credential.save_details()
                                             
                                             the_credential = credentials("Twitter", "Moglieish", "AbCdEfGh")
                                             the_credential.save_details()
                                             credential_is_found = credentials.if_credential_exist("Twitter")
                                             
                                             self.assertTrue(credential_is_found)
                                             
                                             def test_display_all_saved_credentials(self):
                                                 self.assertEqual(credentials.display_credentials(),credentials.credentials_list)
                                                 
                                                 if __name__ == "__main__":
    unittest.main()