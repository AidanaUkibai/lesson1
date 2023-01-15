import sys

from users.services import UserServices
from users.repositories import UserRepositories
from users.handlers import UserHandlers

def init():
    user_repositories =UserRepositories()
    user_services = UserServices(user_repositories)
    user_handlers = UserHandlers(user_services)

    while True:
        print("1.Регистрация Админа: (sign_up)")
        print("2.Проверка админа: (sign_up)")
        print("3.Если в нашей базе есть админ то сразу откроется командная строка")
        print("4.C: 'Введите команды:'  ")
        command = input("Введите команду или q (выход): ")

        if command == 'q':
            sys.exit(0)

        if command == 'sign_up':
            username,password = input("Введите username и password:  ").split()
            user_handlers.sign_up(username,password)

        # elif command == 'ch':
        #     username,o_password,n_password=input("enter: ").split()
        #     user_handlers.change_password(username, o_password, n_password)


        elif command == "sign_in":
            username,passwords = input("Пожалуйста, введите данные: ").split()
            user_handlers.sign_in(username,password)

        # elif command == "cmd":
        #     username = input("Please, enter your username: ")
        #     user_handlers.check_cmd()




        else:
            print("invalid command, try again")


if __name__=='__main__':
    init()
