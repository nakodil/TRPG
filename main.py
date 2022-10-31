import os
from game import Game


class Menu:
    def __init__(self):
        self.main_loop()

    def main_loop(self):
        while True:
            os.system("cls")
            print("Текстовая игра")
            print("«Приключения Васи Питонова»\n")

            print("1. Начать новую игру")
            print("2. Загрузить старую игру")
            print("3. Посмотреть авторов игры")
            print("4. Настройки")
            print("0. Выйти из игры")

            option = input("\nВведите номер варианта и нажмите ENTER: ")
            if option == "1":
                game = Game()
            elif option == "2":  # DRY!
                os.system("cls")
                print("Загрузка игры не реализована")
                input("\nНажмите ENTER чтобы продолжить")
            elif option == "3":
                os.system("cls")
                print("Игра сделана в кружке «Информационные технологии»")
                input("\nНажмите ENTER чтобы продолжить")
            elif option == "4":
                os.system("cls")
                print("Настройки не реализованы")
                input("\nНажмите ENTER чтобы продолжить")
            elif option == "0":
                os.system("cls")
                print("Спасибо за игру!")
                break


if __name__ == "__main__":
    Menu()
