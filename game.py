from random import randint, choice
from os import system

class Item:
    """
    Переопределить __repr__ ?
    """
    def __init__(self):
        self.name = "Предмет"
        self.description = "Описание предмета"

    def show(self):
        print(self.name, end=", ")


class Inventory:
    def __init__(self):
        self.items=[]

    def show(self):
        print("Инвентарь: ", end="")
        if self.items:
            for item in self.items:
                item.show()
        else:
            print("пусто")

    def get_filtered_by_class(self, *filters):
        [item for item in self.items if isinstance(item, Consumable())]


class Weapon(Item):
    def __init__(self, attack_gain):
        super().__init__()
        self.attack_gain = attack_gain


class Shield(Item):
    def __init__(self, defence_gain):
        super().__init__()
        self.defence_gain = defence_gain


class Consumable(Item):
    def __init__(self, hp_gain):
        super().__init__()
        self.hp_gain = hp_gain


class Character:
    first_names = ("Жран", "Жлыг", "Грог", "Дрын", "Урк", "Брысь")
    last_names = ("Борзый", "Свирепый", "Зловонный", "Гнусный", "Скверный", "Гадский")

    def __init__(
        self,
        name=f"{choice(first_names)} {choice(last_names)}",
        hp=randint(1, 100),
        xp=0,
        weapon=Weapon(2),
        shield=Shield(3),
        attack=randint(1, 100),
        defence=randint(1, 100),
        luck=randint(1, 100),
        money=randint(0, 1000),
        inventory=Inventory()
    ):
        self.name = name
        self.hp = hp
        self.xp = xp
        self.weapon = weapon
        self.shield = shield
        self.attack = attack
        self.defence = defence
        self.luck = luck
        self.money = money
        self.inventory = inventory
    
    def show(self):
        print(f"имя: {self.name}")
        print(f"здоровье: {self.hp}")
        print(f"опыт: {self.xp}")
        print(f"оружие: {self.weapon.name} — {self.weapon.description}")
        print(f"щит: {self.shield.name} — {self.shield.description}")
        print(f"атака: {self.attack}")
        print(f"защита: {self.defence}")
        print(f"удача: {self.luck}")
        print(f"деньги: {self.money}")
        self.inventory.show()
        print("")

    def consume_item(self, item_inventory_idx):
        """
        TODO: Передать эффекты употребленного предмета игроку
        Метод игрока или инвентаря?
        """
        item = self.inventory.items[item_inventory_idx]
        print(f"{self.name} употребил {item.name} и восстановил {item.hp_gain}")
        self.inventory.items.pop(item_inventory_idx)


# тестируем игрока
player = Character(name="Вася Питонов", hp=100, xp=0, attack=1, defence=1, luck=1, money=100)
player.inventory.items = [Consumable(5), Consumable(13), Weapon(7), Shield(3)]

system("cls")
player.show()

input("\nНажмите ENTER чтобы употребить предмет 0")

system("cls")
player.consume_item(0)
player.show()
