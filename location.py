from hero import Hero  # для создания противника на Арене


class Location:
    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.options = options

    def show(self):
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
    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.options = options
        self.price = 10
        self.options["1"] = ("Купить зелье", "купить")

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


if __name__ == "__main__":
    hub = Location(id="1", description="desc", options={})
    shop = Shop(id="2", description="desc", options={})