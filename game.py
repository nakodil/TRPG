import os
from hero import Hero
from item import Weapon, Shield, Potion
import location


class Game:
    def __init__(self):
        """
        Создает локации
        Создает героя
        Запускает главный цикл игры
        """

        # создаем игрока
        self.player = Hero(
            name="Вася Питонов",
            hp=100,
            xp=0,
            money=500,
            attack=2,
            defence=1,
            inventory=[Weapon(), Shield(), Potion()]
        )

        # создаем локации
        hub = location.Location(
            id="хаб",
            description=f"{self.player.name} приехал в Хаб.",
            options={
                "1": ("Поехать на арену", "арена"),
                "2": ("Заглянуть в лавку алхимика", "лавка"),
                "3": ("Сыграть в кости", "кости"),
                "0": ("Выйти в главное меню без сохранения", "меню")
            }
        )
        shop = location.Shop(
            id="лавка",
            description=f"{self.player.name} приехал в лавку алхимика.",
            options={
                "1": ("Купить зелье", "купить"),
                "2": ("Вернуться в Хаб", "хаб"),
                "0": ("Выйти в главное меню без сохранения", "меню")
            }
        )
        arena = location.Arena(
            id="арена",
            description=f"{self.player.name} приехал на арену.",
            options={
                "1": ("Выйти на битву с разбойником", "бой"),
                "2": ("Вернуться в Хаб", "хаб"),
                "0": ("Выйти в главное меню без сохранения", "меню")
            }
        )

        # сохраняем все локации в экземпляре Game
        self.locations = {
            "хаб": hub,
            "лавка": shop,
            "арена": arena
        }

        # запускаем главный цикл игры
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
            # В бою здесь нужно показать противника. Переопределить show у Arena?
            self.location.show()
            self.location.choose_option(self.player)
