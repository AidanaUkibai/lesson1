from typing import Optional

from users.models import User
from users.services import UserServices
import os
import sys
from fnmatch import fnmatch

#base_path = os.path.basename("D:\Element School\lesson1\lesson8\users")

class UserHandlers:

    def __init__(self, services: UserServices):
        self.services = services

    def sign_up(self, username:str, password:str)-> None:
        username= username.strip()
        password = password.strip()

        if len(password)<8:
            print("The password  is too short")
            return

        if self.services.is_authentificated(username):
            return self.check_cmd()


        self.services.creat_user(username, password)



    def sign_in(self,username:str,password: str)-> Optional[User]:
        return self.services.get_user(username, password)

    @staticmethod
    def check_cmd():
        base_path = os.path.basename("D:\\Element School\\lesson1\\lesson8\\users")
        def main(com):
            values = com.split(" ")

            return values

        while True:
            command = input("C: ")
            values = main(command)

            if values[0] == "dir":
                with os.scandir(base_path) as entries:
                    for entry in entries:
                        print(entry.name)
                # return pp

            elif values[0] == "cd":
                with os.scandir(base_path) as entries:
                    for entry in entries:
                        # print(entry.name)
                        # try:
                        if entry.name == values[1]:
                            # base_path = os.path.join(base_path, values[1])
                            with os.scandir(os.path.join(base_path, values[1])) as entries1:
                                base_path = os.path.join(base_path, values[1])
                                for entry1 in entries1:
                                    print(entry1.name)




            elif values[0] == "cd..":
                with os.scandir(base_path) as entries:
                    for entry in entries:
                        print(entry.name)
                # os.chdir(base_path)

            elif values[0] == "rd":
                with os.scandir(base_path) as entries:
                    for entry in entries:
                        if fnmatch(entry.name, values[1]):
                            os.remove(os.path.join(base_path, entry.name))


            elif values[0] == "touch":
                u = input()
                with os.scandir(base_path) as entries:
                    with open(u, 'w') as f:
                        text = input()
                        print(f.write(text))


            elif values[0] == "rename":
                t = input()
                o = input()
                with os.scandir(base_path) as entries:
                    for entry in entries:
                        # print(entry.name)
                        if entry.name == t:
                            os.rename(os.path.join(base_path, entry.name), os.path.join(base_path, o))
                        else:
                            print("exception")


            elif values[0] == "ch":
                p = input()
                with os.scandir(base_path) as entries:
                    for entry in entries:
                        if fnmatch(entry.name, p):
                            with open(os.path.join(base_path, entry.name), 'r') as f:
                                print(f.read())

            elif values[0] == "exit":
                sys.exit(0)

                # elif values[0] == "cd":
                #     with os.scandir("D:\Element School\lesson1\proect\C") as entries:
                #                 for entry in entries:
                #                    print(entry.name)

            else:
                print("Неизвестно как эти данные обработать")

    # def change_password(self,username:str,old_password:str,new_password:str):
    #     username = username.strip()
    #     old_password = old_password.strip()
    #     new_password = new_password.strip()
    #
    #
    #     if len(old_password)<8 and len(new_password)<8:
    #         print("The password  is too short")
    #         return
    #
    #     if self.services.check_user_exists(username):
    #         print('User already exists!')
    #         return
    #     self.services.change_password(username,old_password,new_password)