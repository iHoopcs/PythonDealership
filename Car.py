# Car class for Main.py
class Car:
    def __init__(self, make, model, num_doors, color, year):
        # Default values assigned after 'or'
        self.make = make or 'unknown'
        self.model = model or 'unknown'
        self.num_doors = num_doors or 4
        self.color = color or 'Black'
        self.year = year or 2023

    # Function that formats output w/ labels for display car & features
    def to_string(self) -> str:
        output = 'Make: ' + self.make + '\n'
        output += 'Model: ' + self.model + '\n'
        output += '#ofDoors: ' + self.num_doors + '\n'
        output += 'Color: ' + self.color + '\n'
        output += 'Year: ' + self.year

        return output

    # Function to format output to save to file
    def save(self) -> str:
        return self.make + ' | ' + self.model + ' | ' + str(self.num_doors) + ' | ' + self.color + ' | ' + str(self.year) + '\n'




