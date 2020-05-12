# heart-rate.py
# prototype heart-rate tracker for fitness watch
# By: Tony Huang
# Created 5/5/2020
# Last modified 5/5/2020
# version 0.5


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

    resting_rate = int_input("What is your resting heart rate in bpm?: ")
    max_rate = int_input("What is your maximum heart rate in bpm?: ")

    reserve_rate = max_rate - resting_rate

    #Returns heart rate range between resting and maximum
    return(reserve_rate, resting_rate, max_rate)


def minute_update(resting_rate, max_rate):
    "Returns the average heart rate of a period of exercise"
    timer = 1
    heart_rates = [] #Stores all heart rates


    while True:    
        heart_rate = int_input("What is you heart rate at minute {}: ".format(timer))
        if heart_rate <= max_rate and heart_rate >= resting_rate: #Checks if heartrate input is between resting and max
            heart_rates.append(heart_rate)
            timer += 1
        else:
            print("Invalid input: heart rate input should be between maximum and resting rate")

        if input("Press y to exit the programme or anything else to continue") == "y":
            return(sum(heart_rates)/len(heart_rates)) #Finds the average of the list by dividng the sum of values by number of values


def intensity(reserve_rate, resting_rate, max_rate, average_rate):
    """Determins intensity of exercise based of heart_rate input"""

    easy_boundary = int(reserve_rate * 0.3)
    moderate_boundary = int(reserve_rate * 0.6)
    hard_boundary = int(reserve_rate * 0.9)

    # Dictionary establishes the difficulty levels and their range
    intensities = {"very easy": [resting_rate,  easy_boundary],
        "easy": [easy_boundary, moderate_boundary],
        "moderate": [moderate_boundary, hard_boundary],
        "hard": [hard_boundary, max_rate]}

    # Increments through dictionary keys and checks if the average rate is inside the range
    for key in intensities:
        if average_rate >= intensities.get(key)[0] and average_rate <= instensities.get(key)[1]:
            return(key)


def exercise_selector():
    """Allows user to select the exercise they are performing"""


def output():
    """Disaplays completed exercise, length of time, and intensity"""


def main():
    """Main sequence"""
    reserve_rate, resting_rate, max_rate = resting_max()
    average_rate = minute_update(resting_rate, max_rate)

    print(intensity(reserve_rate, resting_rate, max_rate, average_rate))


main()
