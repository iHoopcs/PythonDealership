import sys


# Car Class -> class specific features/attributes
class Car:
    def __init__(self, make, model, num_doors, color, year):
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.color = color
        self.year = year


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

    elif choice == '2':  # Delete car
        # Delete Function
        print('Delete Car')

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





