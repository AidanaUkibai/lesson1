from typing import List, Optional

from users.models import User


class UserRepositories:
    users: List[User]=[]

    def is_authentificated(self,username)-> bool:
        return bool(next((u for u in self.users if u.username == username), None))

    def creat_user(self,username: str, password: str) -> None:
        user = User(username)
        user.set_password(password)
        self.users.append(user)
        #return user

    def get_user(self,username: str, password: str) -> Optional[User]:
        user = next((u for u in self.users if username == u.username and u.check_password(password)), None)

        if not user:
            print('User not found')
            return

        return user

    # def check_cmd(self,username: str, password: str):
    #     user = next((u for u in self.users if username == u.username and u.check_password(password)), None)
    #
    #     if not user:
    #         print('User not found')
    #         return
    #
    #     return






    # def change_password(self,username:str,old_password:str,new_password: str)->None:
    #     user = next((u for u in self.users if username == u.username and u.check_password(old_password)), None)
    #     user.set_password(new_password)
    #     self.users.append(user)






