from location import Location


class Hub(Location):
    def __init__(self):
        super().__init__()
        self.id = "хаб"
        self.description = "Хаб"
        self.options["1"] = ("Биться на арене", "арена")
        self.options["2"] = ("Зайти в лавку алхимика", "лавка")
        self.options["3"] = ("Сыграть в кости", "казино")
        self.options["0"] = ("Выйти в меню без сохранения игры", "меню")
        Location.locations[self.id] = self

"""
def visit(player, game):
    while game:
        cls()
        print(f"game сейчас {game}")
        print(f"{player.name} приехал к камню.")
        print("1. Поехать на арену")
        print("2. Отправиться в казино")
        print("3. Зайти в лавку алхимика")
        print("0. Выйти в главное меню")
        player.show()
        option = choose_option()
        if option == "1":
            arena.visit(player, game)
        elif option == "2":
            casino.visit(player, game)
        elif option == "3":
            shop.visit(player, game)
        elif option == "0":
            game = False
            input("Перед return Хаба")
            return
"""