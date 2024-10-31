class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor, number_of_floors):
        if new_floor <= number_of_floors and new_floor >= 1:
            print(new_floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
       return self.number_of_floors

    def __str__(self):
        return (f'Название:, {self.name}, количество этажей: {self.number_of_floors}')


building = House('ЖК Эльбрус', 30)
building_1 = House('ЖК Казбек', 20)

building.go_to(18, 30)
building_1.go_to(15,20)

print(building)
print(building_1)
print(len(building))
print(len(building_1))