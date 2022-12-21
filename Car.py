# Car class for Main.py
class Car:
    def __init__(self, make, model, num_doors, color, year):
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.color = color
        self.year = year

    def to_string(self) -> str:
        output = ''
        output += 'Make: ' + self.make + '\n'
        output += 'Model: ' + self.model + '\n'
        output += '#ofDoors: ' + self.num_doors + '\n'
        output += 'Color: ' + self.color + '\n'
        output += 'Year: ' + self.year

        return output



