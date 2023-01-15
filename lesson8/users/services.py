from typing import Optional

from users.repositories import UserRepositories

from users.models import User


class UserServices:

    def __init__(self,repositories: UserRepositories):
        self.repositories=repositories

    def is_authentificated(self,username)-> bool:
        return self.repositories.is_authentificated(username)

    def creat_user(self,username: str, password: str) -> None:
        self.repositories.creat_user(username,password)
        self._send_email_to_user(username)



    def get_user(self,username: str, password: str) -> Optional[User]:
        user= self.repositories.get_user(username,password)
        self._check_user_device()
        return user

    # def change_password(self, username: str, old_password: str, new_password: str) -> None:
    #     user=self.repositories.change_password(username,old_password,new_password)
    #     self._change_p()
    #     return user

    @staticmethod
    def _send_email_to_user(username:str)-> None:
        print(f'send verification letter to {username}')

    def _check_user_device(self):
        print('logged in by Iphone')

    def _change_p(self):
        print("Sucessful logged")