from user.singleton import Singleton

#This is the User class, has inherited from a metaclass "type"
class User(metaclass=Singleton):

    def __init__(self,login):
            self.login = login
