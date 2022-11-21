import os
from game import *

p1 = Character(name="Вася Питонов", hp_now=100, xp_now=0, attack=1, defence=1, luck=1, money=100)
p1.inventory.append(Consumable(name="Малое зелье здоровья", hp_mod=10))
p1.inventory.append(Consumable(name="Малое зелье здоровья", hp_mod=10))
p1.inventory.append(Consumable(name="Среднее зелье здоровья", hp_mod=50))
p1.inventory.append(Weapon(name="Кибербогатырский меч", attack_mod=3))
p1.inventory.append(Shield(name="Дубощит", defence_mod=2))
p1.weapon = Weapon(name="Обычный меч", attack_mod=1)
p1.shield = Shield(name="Обычный щит", defence_mod=1)
p1.calculate_stats()

game = True
while game:
    os.system("cls")
    p1.show()
    item_idx = int(input("\nВведите номер варианта и нажмите ENTER: "))
    p1.equip_item(item_idx)
    input("\nENTER - дальше")
