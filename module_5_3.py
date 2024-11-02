class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
       return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, other):
        return House( self.name, self.number_of_floors + other)
    def __iadd__(self, other):
        return House( self.name, self.number_of_floors + other)
    def __radd__(self, other):
        return House( self.name, self.number_of_floors + other)

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


building = House('ЖК Эльбрус', 10)
building_1 = House('ЖК Акация', 20)

print(building)
print(building_1)
print(building == building_1)

building = building +10
print(building)
print(building == building_1)

building += 10
print(building)

building_1 = 10 + building_1
print(building_1)

print(building > building_1)
print(building >= building_1)
print(building < building_1)
print(building <= building_1)
print(building != building_1)