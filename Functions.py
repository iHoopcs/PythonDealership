# Class holding functions accessible by main.py

from Car import Car


# Functions for Main.py

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
        print("\nPlease enter the corresponding number for the car you'd like to delete, enter a dash to go back.")
        for number, index in enumerate(array):
            print(number, ' - ' + index.make + ' ' + index.model)  # number variable controls numbering list in order

        deletion_choice = input()
        if deletion_choice == '-':
            pass
            print(' ')

        else:
            # Cast str -> int to use in array index call
            deletion_choice = int(deletion_choice)
            deleted_car_display_name = array[deletion_choice].make + ' ' + array[deletion_choice].model
            del (array[deletion_choice])
            print('*' + deleted_car_display_name + ' successfully removed*\n')


# Function to edit features of user specified car object
def edit_car(array: Car):
    print("\nPlease enter the corresponding number for which car you'd like to edit, enter a dash to go back.")
    display_cars(array)
    edit_choice = input()

    if edit_choice == '-':
        pass
        print(' ')
    else:
        # Cast str -> int to use in array index call
        edit_choice = int(edit_choice)
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


# Function to further inspect car features based on user selection - function call after display_cars() - menu option 4
def view_car(array: Car):
    print("Please enter the corresponding number for which car you'd like to further inspect, enter a dash to go back.")
    inspect_choice = input()

    if inspect_choice != '-':
        # Cast str -> int to use in array index call
        inspect_choice = int(inspect_choice)
        # If user doesn't choose main menu, display selected car features
        print(array[inspect_choice].to_string())
    else:
        pass
        print(' ')


# Function to save car objects & features to file
def save_car(array: Car):
    car_file = open('Cars.txt', 'w')

    for i in array:
        car_file.write(i.save())
    print('\n*Cars & features saved*')


# Function to read Cars.txt -> take information and import car objects w/ features into program
def load_cars():
    # Create array to store car objects w/ features from file
    file_cars = []

    car_file = open('Cars.txt', 'r')

    # Initialize array to store lines of car info
    file_content = []
    file_content = car_file.readlines()

    for i in file_content:
        # If the line read is blank - skip
        if i == '\n':
            pass
        else:
            # each line set to variable
            content_line = i

            # Array to store each car's features
            car_features = []
            car_features = content_line.split(' | ')

            # Retrieve/Assign features
            file_make = car_features[0]
            file_model = car_features[1]
            file_num_doors = car_features[2]
            file_color = car_features[3]
            file_year = car_features[4]

            # Create car object -> add to array
            car = Car(
                file_make,
                file_model,
                file_num_doors,
                file_color,
                file_year
            )

            file_cars.append(car)

    return file_cars
