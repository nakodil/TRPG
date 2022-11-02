class Inventory:
    def __init__(self):
        self.items = []

    def filter_items(self, *by_class):
        """
        Собирает словарь предметов инвентаря, отфильтрованных по их классу
        Если фильтры пустые, собирает в словарь все предметы инвентаря
        Нумерация предметов в словаре начинается с 1
        {"1": ("Имя предмета", "Описание предмета")}
        """
        self.filtered_items = dict()
        if not by_class:
            for num, item in enumerate(self.items, 1):
                self.filtered_items[str(num)] = (item.name, item.description)
        else:
            num = 1
            for filter in by_class:
                for item in self.items:
                    if isinstance(item, filter):
                        self.filtered_items[str(num)] = (item.name, item.description)
                        num += 1

    def show_filtered(self):
        if self.filtered_items:
            for num, item in self.filtered_items.items():
                print(f"{num}. {item[0]}: {item[1]}")
        else:
            print("Нет фильтрованных предметов")

        

class Item:
    pass


class Weapon(Item):
    def __init__(self):
        self.id = "оружие"
        self.name = "Оружие"
        self.description = "Дефолтное оружие"
        self.attack = 1


class Shield(Item):
    def __init__(self):
        self.id = "щит"
        self.name = "Щит"
        self.description = "Дефолтный щит"
        self.defence = 1


class Consumable(Item):
    # TODO: эффект от употребления - в конструктор
    def __init__(self):
        self.id = "зелье"
        self.name = "Зелье"
        self.description = "Дефолтное зелье"
        self.consume_text = f"Вася Питонов выпил {self.name}"


if __name__ == "__main__":
    inventory = Inventory()
    inventory.items.append(Weapon())
    inventory.items.append(Weapon())
    inventory.items.append(Shield())
    inventory.items.append(Consumable())
    inventory.filter_items(Weapon, Consumable)
    inventory.show_filtered()