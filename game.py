import os
from hero import Hero
from location import Location


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
        Location.make_locations()
        self.main_loop()

    def main_loop(self):
        """
        Главный цикл контролирует self.player.is_playing:bool
        Игрок начинает в Хабе
        """
        self.player.location_name = "хаб"
        while self.player.is_playing:
            self.location = Location.locations[self.player.location_name]
            self.player.show()
            # в бою здесь нужно показать противника?
            self.location.show()
            self.location.choose_option(self.player)
