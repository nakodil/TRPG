import os


class Item:
    def __init__(self):
        self.id = "id"
        self.name = "какой-то предмет"


class Weapon(Item):
    def __init__(self):
        self.id = "id оружия"
        self.name = "оружие"


class Shield(Item):
    def __init__(self):
        self.id = "id оружия"
        self.name = "щит"


class Potion(Item):
    def __init__(self):
        self.id = "id оружия"
        self.name = "зелье"
    
    def consume(self, player):
        player.hp += 10
        del self
        os.system("cls")
        print("Вася питонов выпил зелье и восстановил 10 единиц здоровья")
        input("Пауза после зелья")

