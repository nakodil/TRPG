class Hero:
    """
    TODO:
        Определить repr!!!!
        Инвентарь из Item()
        Метод показа инвентаря
        Как статы предметов меняют статы героя?
    """
    def __init__(
        self,
        name="Безымянный",
        hp=100,
        xp=0,
        money=0,
        attack=1,
        defence=1,
        inventory=[],
        location_name="хаб"
    ):
        self.is_playing = True
        self.location_name = location_name
        self.name = name
        self.hp = hp
        self.xp = xp
        self.money = money
        self.attack = attack
        self.defence = defence
        self.inventory = inventory

    def show(self):
        print(f"{self.name}")
        print(f"здоровье: {self.hp}")
        print(f"опыт: {self.xp}")
        print(f"деньги: {self.money}")
        print(f"атака: {self.attack}")
        print(f"защита: {self.defence}")
        self.show_inventory()

    def show_inventory(self):
        print("инвентарь: ", end="")
        if self.inventory:
            for item in self.inventory:
                print(item.name, end=", ")
        else:
            print("пусто")
        print("")
