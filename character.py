from item import Inventory, Weapon, Shield, Consumable


class Character:
    def __init__(
        self,
        id="персонаж",
        name="Персонаж",
        description="Дефолтный персонаж",
        hp=100,
        xp=0,
        attack=1,
        defence=1,
        weapon=Weapon(),
        shield=Shield(),
        inventory=Inventory(),
        money=0
    ):
        self.id = id
        self.name = name
        self.description = description
        self.hp = hp
        self.xp = xp
        self.attack = attack
        self.defence = defence
        self.weapon = weapon
        self.shield = shield
        self.inventory = inventory
        self.money = money

    def show(self):
        print(self.name)
        print(f"описание: {self.description}")
        print(f"жизни: {self.hp}")
        print(f"опыт: {self.xp}")
        print(f"деньги: {self.money}")
        print(f"атака: {self.attack}")
        print(f"защита: {self.defence}")
        print(f"оружие: {self.weapon}")
        print(f"щит: {self.shield}")
        print("инвентарь:")
        self.inventory.filter_items()
        self.inventory.show_filtered()


if __name__ == "__main__":
    player = Character()
    player.inventory.items.append(Consumable())
    player.inventory.items.append(Consumable())
    player.show()