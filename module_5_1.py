class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor, number_of_floors):
        if new_floor <= number_of_floors and new_floor >= 1:
            print(new_floor)
        else:
            print('Такого этажа не существует')


building = House('ЖК Эльбрус', 30)
building.go_to(30, 30)

building_1 = House('ЖК Казбек', 20)
building_1.go_to(20,20)