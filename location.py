import os
from hero import Hero  # для создания противника на Арене
from item import Weapon, Shield, Potion


class Location:
    """
    TODO:
        ASCII-арт из файла для картинок локаций
        Shop и Arena в отдельные модули
    """
    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.image = r"__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___"
        self.options = options

    def show(self):
        """
        Показывает описание и опции текущей локации
        """
        print("\n", self.image)
        print("\n" + self.description)
        for key, value in self.options.items():
            print(f"{key} - {value[0]}")

    def choose_option(self, player):
        """
        Выбирает вариант.
        Вариант изменяет текущую локацию игрока
        или вызывает метод текущей локации (покупка, битва, ...)
        или завершает главный цикл игры с помощью player.is_playing
        """
        option_num = input("\nВведите номер варианта и нажмите ENTER: ")
        if option_num in self.options:
            option_name = self.options[option_num][1]
            if option_name  == "меню":
                player.is_playing = False
            elif option_name == "купить":
                self.buy(player)
            elif option_name == "бой":
                self.fight(player)
            else:
                player.location_name = self.options[option_num][1]


class Shop(Location):
    """
    Расширяет родительский класс полем self.price - ценой зелья и
    методом покупки зелья buy()
    """
    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.image = r"__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___"
        self.options = options
        self.price = 10

    def buy(self, player):
        os.system("cls")
        if player.money >= self.price:
            player.money -= self.price
            player.inventory.append(Potion())
            print(f"{player.name} купил зелье!")
        else:
            print(f"{player.name} не хватило денег!")
        input("\nНажмите ENTER чтобы продолжить")

    def sell(self, player):
        os.system("cls")
        input("\nПродажа не реализована")


class Arena(Location):
    """
    Пользоваться конструктором родительского класса?
    """
    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.image = r"__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___"
        self.options = options

    def fight(self, player):
        """
        Создает противника
        начинает бой
        считает итоги боя
        TODO: рандомизация противника
        """
        self.enemy = Hero(
            name="Жран Борзый",
            hp=100,
            xp=0,
            money=100,
            attack=1,
            defence=0,
            inventory=[Weapon(), Shield()]
        )
        os.system("cls")
        print(f"Бой начался! Против {player.name} сражается {self.enemy.name}!")
        input("\nНажмите ENTER чтобы сделать ход")
        
        # бой
        while player.hp > 0 and self.enemy.hp > 0:
            os.system("cls")
            if player.hp > 0:
                self.combat_turn(player, self.enemy)
            if self.enemy.hp > 0:
                self.combat_turn(self.enemy, player)
            print("")
            player.show()
            print("")
            self.enemy.show()
            input("\nНажмите ENTER чтобы сделать ход")
        
        # итоги боя
        os.system("cls")
        if player.hp > 0 and self.enemy.hp <= 0:
            print(f"В этом бою победил {player.name}! {self.enemy.name} проиграл!")
            # забрать награды за бой
            input("\nНажмите ENTER чтобы вернуться на арену")
        elif player.hp <= 0 and self.enemy.hp > 0:
            player.is_playing = False
            print(f"В этом бою победил {self.enemy.name}! {player.name} проиграл!")
            input("\nНажмите ENTER чтобы выйти в главное меню")
        else:
            print(f"Какой ужас! {player.name} и {self.enemy.name} погибли в этом бою!")
            player.is_playing = False
            input("\nНажмите ENTER чтобы выйти в главное меню")

    def combat_turn(self, attacker, defender):
        """
        staticmethod?
        """
        damage = attacker.attack
        defender.hp -= damage
        print(f"{attacker.name} ударил {defender.name} и нанес ему {damage} урона")


class Casino(Location):
    pass


if __name__ == "__main__":
    hub = Location(id="1", description="desc", options={})
    shop = Shop(id="2", description="desc", options={})