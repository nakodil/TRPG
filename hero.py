class Hero:
    def __init__(
        self,
        name="Безымянный",
        hp=100,
        xp=0,
        money=0,
        attack=1,
        defence=1,
        inventory=[],
        location=None
    ):
        self.is_playing = True
        self.location_name = "хаб"
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
        print(f"инвентарь: {self.inventory}")
