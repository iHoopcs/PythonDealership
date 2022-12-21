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
        output += 'Year: ' + self.year

        return output


# Function to display car objects in number list
def display_cars(array: Car):
    if len(array) == 0:
        print('*List empty: No cars to display*')
        print('*Please create/add cars to list*')
    else:
        for number, index in enumerate(array):
            print(number, ' - ' + index.make + ' ' + index.model)


# Function to create car object
def create_car() -> Car:
    print('\nLets create a car!')
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
        print('*Please create/add cars to list*\n')
    else:
        print("\nPlease enter the corresponding number for the car you'd like to delete.")
        for number, index in enumerate(array):
            print(number, ' - ' + index.make + ' ' + index.model) # number variable controls numbering list in order

        deletion_choice = int(input())
        deleted_car_display_name = array[deletion_choice].make + ' ' + array[deletion_choice].model
        del(array[deletion_choice])
        print('*' + deleted_car_display_name + ' successfully removed*\n')


# Function to edit features of user specified car object
def edit_car(array: Car):
    print("\nPlease enter the corresponding number to which car you'd like to edit")
    display_cars(array)
    edit_choice = int(input())

    print("\nAccessing " + array[edit_choice].make + ' ' + array[edit_choice].model + "'s features...")
    # Display selected car object's features to edit
    print(array[edit_choice].to_string())

    print('\nWhich feature would you like to edit?')
    print('1 - Make')
    print('2 - Model')
    print('3 - Number of Doors')
    print('4 - Color')
    print('5 - Year')
    feature_choice = input()

    # Menu Logic
    if feature_choice == '1':
        print('\nCurrent Make: ' + array[edit_choice].make)
        new_make = input('New Make: ')
        array[edit_choice].make = new_make
        print('*Successfully changed to ' + new_make)

    elif feature_choice == '2':
        print('\nCurrent Model: ' + array[edit_choice].model)
        new_model = input('New Model: ')
        array[edit_choice].model = new_model
        print('Successfully changed to ' + new_model)

    elif feature_choice == '3':
        print('\nCurrent Number of Doors: ' + array[edit_choice].num_doors)
        new_num_doors = input('New Number of Doors: ')
        array[edit_choice].num_doors = new_num_doors
        print('Successfully changed to ' + new_num_doors)

    elif feature_choice == '4':
        print('\nCurrent Color: ' + array[edit_choice].color)
        new_color = input('New Color: ')
        array[edit_choice].color = new_color
        print('Successfully changed to ' + new_color)

    elif feature_choice == '5':
        print('\nCurrent Year: ' + array[edit_choice].year)
        new_year = input('New Year: ')
        array[edit_choice].year = new_year
        print('Successfully changed to ' + new_year)
    else:
        print('INVALID INPUT')
        edit_car(array)

    print('*Updated Car Features*\n')
    print(array[edit_choice].to_string() + '\n')


# Initialize empty array to store car objects
car_array: Car = []
print('Welcome to the Python Dealership!')
# Main Menu
while True:
    print('What would you like to do?')
    print('1 - Create a car')
    print('2 - Delete a car')
    print('3 - Edit an existing car')
    print('4 - View available cars')
    print('5 - Save & Exit')
    choice = input()

    if choice == '1':  # Create car
        # Create new car calling function -> add to array
        car = create_car()
        car_array.append(car)
        print('*' + car.make + ' ' + car.model + ' successfully created & added to list*\n')

    elif choice == '2':  # Delete car
        # Delete Function
        delete_car(car_array)

    elif choice == '3':  # Edit car
        # Edit Function
        edit_car(car_array)

    elif choice == '4':  # View cars
        # Display Function
        print('\nLoading available cars...')
        display_cars(car_array)
        print(' ')

    elif choice == '5':  # Save & Exit
        # Save Function
        print('Thank you! Goodbye!')
        sys.exit()





