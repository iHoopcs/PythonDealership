import sys
from Car import Car
from Functions import create_car, delete_car, edit_car, display_cars, save_car,view_car

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
        view_car(car_array)
        print(' ')

    elif choice == '5':  # Save & Exit
        # Save Function
        if len(car_array) == 0:
            print('*List empty: No cars saved*')

        else:
            save_car(car_array)

        print('Thank you! Goodbye!')
        sys.exit()





