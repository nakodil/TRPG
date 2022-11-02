from scene import Scene 
from character import Character
from item import Weapon, Shield, Potion


class Game:
    """
    очищает экран?
    создает персонажа
    показывает персонажа
    показывает сцену
    показывает опции
    """
    def __init__(
        self,
        current_scene_name=None,
        player=None,
    ):
        self.current_scene_name = current_scene_name
        self.player = player

    def make_player(self):
        self.player = Character(
            id="игрок",
            name="Вася Питонов",
            description="Кибербогатырь в поисках приключений",
            hp=100,
            xp=0,
            attack=1,
            defence=1,
            weapon=Weapon(),
            shield=Shield(),
            inventory=[Potion()],
            money=50
        )

    def make_scences(self):
        self.scenes = [
            Scene(
                id="хаб",
                name="Хаб",
                description="Хаб - место, где оказываются все кибербогатыри в поисках приключений.",
                options=[
                    ("Заглянуть в лавку алхимика", "лавка"),
                    ("Выйти в главное меню", "меню")
                ]
            ),
            Scene(
                id="лавка",
                name="Лавка алхимика",
                description="Хоть кибербогатыри и не чувствуют запахов, но в этой лавке как-то странно пахнет!",
                options=[
                    ("Купить зелье", "купить"),
                    ("Уйти в Хаб", "хаб")
                ]
            )
        ]