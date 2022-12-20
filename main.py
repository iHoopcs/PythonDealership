import sys


# Car Class -> class specific features/attributes
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
        output += 'Year: ' + self.year + '\n'


# Function to create car object
def create_car() -> Car:
    print('Please fill out the form below to create your new car.')
    make = input('Make: ')
    model = input('Model: ')
    num_doors = input('Number of Doors: ')
    color = input('Color: ')
    year = input('Year: ')

    new_car = Car(make, model, num_doors, color, year)
    return new_car


# Function to delete user specified car object
def delete_car(array: Car):
    if len(array) == 0:
        print('*List Empty: No cars to display*')
        print('*Please create/add cars to list*')
    else:
        print("\nPlease enter the corresponding number for the car you'd like to delete.")
        for number, index in enumerate(array):
            print(number, ' - ' + index.make + ' ' + index.model) # number variable controls numbering list in order

            deletion_choice = int(input())
            deleted_car_display_name = array[deletion_choice].make + ' ' + array[deletion_choice].model
            del(array[deletion_choice])
            print('\n*' + deleted_car_display_name + ' successfully removed*')


# Initialize empty array to store car objects
car_array: Car = []

# Main Menu
while True:
    print('\nWelcome to the Python Dealership!')
    print('What would you like to do?')
    print('1 - Create a car')
    print('2 - Delete a car')
    print('3 - Edit an existing car')
    print('4 - View available cars')
    print('5 - Save & Exit')
    choice = input()

    if choice == '1':  # Create car
        print('Lets create a car!')
        # Create new car calling function -> add to array
        car = create_car()
        car_array.append(car)
        print('*' + car.make + ' ' + car.model + ' successfully created & added to list*')

    elif choice == '2':  # Delete car
        # Delete Function
        delete_car(car_array)

    elif choice == '3':  # Edit car
        # Edit Function
        print('Edit Car')

    elif choice == '4':  # View cars
        # Display Function
        print('\nLoading available cars...')

    elif choice == '5':  # Save & Exit
        # Save Function
        print('Thank you! Goodbye!')
        sys.exit()





