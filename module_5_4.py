class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        House.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return  f'{self.name}, {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')


building1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
building2 = House('ЖК Акация', 20)
print(House.houses_history)
building3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del building2
del building3
print(House.houses_history)

