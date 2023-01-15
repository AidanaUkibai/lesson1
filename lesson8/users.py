import hashlib


users: list['User']=[]


class User:
    username:str
    __password:str

    def __init__(self,username:str):
        self.username=username


    def set_password(self,password:str):
        self.__password=self._hash_password(password)

    def check_password(self,password:str)->bool:
        return self.__password==self._hash_password(password)

    @staticmethod
    def _hash_password(password: str):
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

    def __repr__(self):
        return f'{self.username} {self.__password}'

# user =User(username='Aidana_Ukibai')
# user.set_password("aviata123")
# print(user)

def creat_user(username:str,password:str)->User:
    user=User(username)
    user.set_password(password)
    users.append(user)

    return user

def get_user(username:str,password:str)-> User or None:
    user =next((u for u in users if username == u.username and u.check_password(password)),None)

    if not user:
        print('User not found')
        return

    return user


us,ps=input("Enter username and password: ").split(' ')
user=creat_user(us,ps)
print(user)
print(users)

us1,ps1=input("Enter username and creds:").split(" ")
print(get_user(us1,ps1))