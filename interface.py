

# class PasswordManager:
#     def __init__(self):
#         self.key = None
#         self.password_file = None
#         self.password_dict = {}

#         def create_key(self,path):
#             self.key = generate_key()
#             with open(path,'wb') as f:
#                 f.write(self.key)

#         def create_password_file(self, path,initial_values=None):
#             self.password_file =path

#             if initial_values is not None:
#                 for key, value in initial_values.items():
#                     self.add_password(key, value) 
#                 def load_password_file(self, path):
#                     self.password_file = path

#                     with open (path,'r')as f:
#                         for line in f:
#                             site, encrypted = line.split(":")
#                             self.password_dict[site] = Password

#                             if self.password_file is not None:
#                                 with open(self.password_file, 'a+') as f:
#                                     encrypted = Fernet(self.key).encrypt(password.encode())
#                                     f.write(site + ":" + encrypted.decode() + "\n")

#                 def get_password (self,site):
#                     return self.password_dict[site]

#                 def main():
#                     password = {
#                         "email": "12346",
#                         "youtube": "helloworld1235",
#                         "instagram": "myfavoritepassword_124"
#                     }
#                     pm = PasswordManager()
#                     print

#                     done = False
#                     while not done:
#                         def http_status(status):
#                             match status:
#                                 case 400:
#                                     return ":"
#                                 case 401:
#                                     return ":"
#                                 case 402:
#                                     return ":" 



