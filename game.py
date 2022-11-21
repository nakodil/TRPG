from random import randint, choice


class Item:
    def __init__(self):
        self.name = "Предмет"
        self.description = "Описание предмета"


class Weapon(Item):
    def __init__(self, name="Оружие", attack_mod=0):
        super().__init__()
        self.name = name
        self.attack_mod = attack_mod


class Shield(Item):
    def __init__(self, name="Щит", defence_mod=0):
        super().__init__()
        self.name = name
        self.defence_mod = defence_mod


class Consumable(Item):
    def __init__(self, name="Зелье", hp_mod=0):
        super().__init__()
        self.name = name
        self.hp_mod = hp_mod


class Character:
    first_names = ("Жран", "Жлыг", "Грог", "Дрын", "Урк", "Брысь")
    last_names = ("Борзый", "Свирепый", "Зловонный", "Гнусный", "Скверный", "Гадский")

    def __init__(
        self,
        name=None,
        lvl=1,
        xp_now=0,
        hp_now=None,
        hp_max=None,
        weapon=None,
        shield=None,
        attack=1,
        defence=1,
        luck=1,
        money=100,
        inventory=None
    ):
        self.name = name
        if not self.name:
            self.name = choice(Character.first_names) + " " + choice(Character.last_names)

        self.lvl = lvl
        self.xp_now = xp_now
        self.xp_next = int((self.lvl + 1) * self.lvl / 2 * 100)

        self.hp_now = hp_now
        if not self.hp_now:
            self.hp_now = randint(1, 100)

        self.hp_max = hp_max
        if not self.hp_max:
            self.hp_max = self.hp_now

        self.inventory = inventory
        if not self.inventory:
            self.inventory = []

        self.weapon = weapon
        self.shield = shield
        self.attack = attack
        self.defence = defence
        self.luck = luck
        self.money = money

    def calculate_stats(self):
        if self.weapon:
            self.attack += self.weapon.attack_mod
        if self.shield:
            self.defence += self.shield.defence_mod

    def show(self):
        print(f"имя: {self.name}")
        print(f"уровень: {self.lvl}")
        print(f"здоровье: {self.hp_now} / {self.hp_max}")
        print(f"опыт: {self.xp_now} / {self.xp_next}")
        if self.weapon:
            print(f"оружие: {self.weapon.name} ({self.weapon.attack_mod})")
        else:
            print("оружие: нет")
        if self.shield:
            print(f"щит: {self.shield.name} ({self.shield.defence_mod})")
        else:
            print("щит: нет")
        print("атака:", self.attack)
        print("защита:", self.defence)
        print("удача:", self.luck)
        print("деньги:", self.money)
        self.show_inventory()
        print("")

    def consume_item(self, inventory_idx):
        """
        TODO: Передать эффекты употребленного предмета игроку
        """
        item = self.inventory[inventory_idx]
        self.hp_now += item.hp_mod
        print(f"{self.name} употребил {item.name} и восстановил {item.hp_mod} здоровья")
        self.inventory.pop(inventory_idx)

    def show_inventory(self):
        print("инвентарь: ", end="")
        """
        if self.inventory:
            counted_items = dict()
            for item in self.inventory:
                if item.name in counted_items:
                    counted_items[item.name] += 1
                else:
                    counted_items[item.name] = 1
            for name, ammount in counted_items.items():
                if ammount  > 1:
                    print(f"{name} x {ammount}", end=", ")
                else:
                    print(name, end=", ")
        """
        if self.inventory:
            for num, item in enumerate(self.inventory):
                print(f"{num}. {item.name}", end=", ")
        else:
            print("пусто")

    def filter_by_class(self, *filters):
        filtered_inventory = []
        for item_class in filters:
            filtered_inventory += [item for item in self.inventory if isinstance(item, item_class)]
        print(*filtered_inventory)

    def equip_item(self, idx):
        if idx > -1 and idx <= len(self.inventory):
            if isinstance(self.inventory[idx], Weapon):
                self.attack -= self.weapon.attack_mod
                self.inventory.append(self.weapon)
                self.weapon = self.inventory[idx]
                self.attack += self.weapon.attack_mod
                self.inventory.pop(idx)
            elif isinstance(self.inventory[idx], Shield):
                self.defence -= self.shield.defence_mod
                self.inventory.append(self.shield)
                self.shield = self.inventory[idx]
                self.defence += self.shield.defence_mod
                self.inventory.pop(idx)
            else:
                print("Этот предмет невозможно экипировать")
        else:
            print("В инвентаре нет такого индекса!")

    def fight(self):
        enemy = Character(hp_now=100, xp_now=100, attack=1, defence=1)
    
    def combat_turn(self, attacker, defender):
        if attacker.hp_now > 0 and defender.hp > 0:
            damage = attacker.attack - defender.defence
            defender.hp -= damage
            print(f"{attacker.name} нанес {defender.name} {damage} урона!")


