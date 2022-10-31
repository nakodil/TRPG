import os
from hero import Hero
import location


class Game:
    def __init__(self):
        """
        Создает героя
        Создает локации
        Запускает главный цикл игры
        """
        self.player = Hero(
            name="Вася Питонов",
            hp=100,
            xp=0,
            money=500,
            attack=2,
            defence=1,
            inventory=["меч", "конь"]
        )

        hub = location.Location(
                id="хаб",
                description="Вася Питонов приехал в Хаб.",
                options={
                    "1": ("Сразиться с разбойником", "битва"),
                    "2": ("Заглянуть в лавку алхимика", "лавка"),
                    "3": ("Сыграть в кости", "кости"),
                    "0": ("Выйти в главное меню без сохранения", "меню")
                }
            )
        shop = location.Shop(
                id="лавка",
                description="Вася питонов приехал в лавку алхимика.",
                options={
                    "2": ("Вернуться в Хаб", "хаб"),
                    "0": ("Выйти в главное меню без сохранения", "меню")
                }
            )
        self.locations = {
            "хаб": hub,
            "лавка": shop
        } 
        self.main_loop()

    def main_loop(self):
        """
        Главный цикл контролирует self.player.is_playing:bool
        Игрок начинает в Хабе
        """
        self.player.location_name = "хаб"
        while self.player.is_playing:
            os.system("cls")
            self.location = self.locations[self.player.location_name]
            self.player.show()
            # в бою здесь нужно показать противника?
            self.location.show()
            self.location.choose_option(self.player)
