import os
from hero import Hero  # для создания противника на Арене


class Location:
    locations = dict()

    @classmethod
    def make_locations(cls):
        Location(
            id="хаб",
            description="Вася Питонов приехал в Хаб.",
            options={
                "1": ("Сразиться с разбойником", "битва"),
                "2": ("Заглянуть в лавку алхимика", "лавка"),
                "3": ("Сыграть в кости", "кости"),
                "0": ("Выйти в главное меню без сохранения", "меню")
            }
        )
        Shop(
            id="лавка",
            description="Вася питонов приехал в лавку алхимика.",
            options={
                "1": ("Купить зелье за 10", "купить"),
                "2": ("Вернуться в Хаб", "хаб"),
                "0": ("Выйти в главное меню без сохранения", "меню")
            }
        )

    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.options = options
        Location.locations[self.id] = self

    def show(self):
        os.system("cls")
        print("\n" + self.description)
        for key, value in self.options.items():
            print(f"{key} - {value[0]}")

    def choose_option(self, player):
        """
        как позвать метод локации (наприме, покупку) из выбора?
        """
        option = input("\nВведите номер варианта и нажмите ENTER: ")
        if option in self.options:
            if option == "0":
                player.is_playing = False
            else:
                player.location_name = self.options[option][1]


class Shop(Location):
    def init(self):
        super().__init__()
        self.price = 10

    def buy(self, player):
        if player.money >= self.price:
            player.money -= self.price
            player.inventory.append("зелье")
            print(f"{player.name} купил зелье!")
        else:
            print(f"{player.name} не хватило денег!")
        input("Пауза в магазине")


class Arena(Location):
    def __init__(self):
        self.enemy = Hero(
            name="Жран Борзый",
            hp=100,
            xp=0,
            money=100,
            attack=10,
            defence=0,
            inventory=["семки", "дубина"]
        )
    
    @staticmethod
    def combat_turn(attacker, defender):
        if attacker.hp > 0:
            damage = attacker.attack
            defender.hp -= damage
            print(f"{attacker.name} ударил {defender.name} и нанес ему {damage} урона")
        else:
            print(f"{attacker.name} проиграл! Победил {defender.name}!")


class Casino(Location):
    pass
