# heart-rate.py
# prototype heart-rate tracker for fitness watch
# By: Tony Huang
# Created 5/5/2020
# Last modified 15/5/2020
# version 1.0


def int_input(message):
    """Gets integer input and checks it for validity before returning it"""
    #  This loop will repeat untill return() is completed sucsessfully and exits out of the function
    while True:
        try:
            return(int(input(message)))  # Prompt displayed by input() will be the paramater of the function
        except:
            print("invalid response please try again")


def resting_max():
    """Gets input on users heart rates and calculate reserve rate"""
    
    while True:
        resting_rate = int_input("What is your resting heart rate in bpm?: ")
        max_rate = int_input("What is your maximum heart rate in bpm?: ")

        reserve_rate = max_rate - resting_rate

        # Returns heart rate range between resting and maximum
        if max_rate > resting_rate > 0:
            return(reserve_rate, resting_rate, max_rate)
        else:
            print("Invalid response, max must be larger than resting")


def minute_update(resting_rate, max_rate):
    "Returns the average heart rate of a period of exercise"
    timer = 1
    heart_rates = []  # Stores all heart rates


    while True:    
        heart_rate = int_input("What is you heart rate at minute {}: ".format(timer))
        if heart_rate <= max_rate and heart_rate >= resting_rate:  # Checks if heartrate input is between resting and max
            heart_rates.append(heart_rate)
            timer += 1
        else:
            print("Invalid input: heart rate input should be between maximum and resting rate")

        if input("Press enter if done or anything else to add another value") == "":
            return(sum(heart_rates)/len(heart_rates), timer)  # Finds the average of the list by dividng the sum of values by number of values


def intensity(reserve_rate, resting_rate, max_rate, average_rate):
    """Determins intensity of exercise based of heart_rate input and returns it"""

    easy_boundary = int(reserve_rate * 0.3)
    moderate_boundary = int(reserve_rate * 0.6)
    hard_boundary = int(reserve_rate * 0.9)


    # Dictionary establishes the difficulty levels and their range
    intensities = {"very easy": [0,  easy_boundary],
        "easy": [easy_boundary, moderate_boundary],
        "moderate": [moderate_boundary, hard_boundary],
        "hard": [hard_boundary, reserve_rate]}

    # Increments through dictionary keys and checks if the average rate is inside the range
    for key in intensities:
         if intensities.get(key)[0] <= (average_rate - resting_rate) <= intensities.get(key)[1]:
            return(key)


def exercise_selector():
    """Allows user to select the exercise they are performing"""

    exercises = {"1": "running", "2": "walking", "3": "resistance trainig", "4": "hiking", "5": "Wii Sports Resort™"}

    while True:
        print("Please select an exericse by pressing the corresponing number")
        selected_exercise = input(exercises).strip() 

        if selected_exercise in exercises: # Checks if User input is in the dictionary
            return(exercises[selected_exercise])
        else:
            print("Invalid input please try again")


def output(exercise):
    """Prints out final output values"""

    reserve_rate, resting_rate, max_rate = resting_max()
    average_rate, duration = minute_update(resting_rate, max_rate)

    intensity_level = intensity(reserve_rate, resting_rate, max_rate, average_rate)

    print("Resting BPM: {}, Max BPM: {}, Average BPM: {}, Exercise: {}, Difficulty: {}, Duration, {}".format(resting_rate, max_rate, average_rate, exercise, intensity_level, duration))


def main():
    """Main sequence, displays menu and selection options """
    exercise = "unspecified"

    while True:
        menu_option = input("1: Change exercise, currently '{}', \n2: Track workout, \n3: Exit \n: ".format(exercise)).strip()
        if menu_option == "1":
            exercise = exercise_selector()
        elif menu_option == "2":
            output(exercise)
        elif menu_option == "3":
            break
        else:
            print("Invalid input please try again")


main()
