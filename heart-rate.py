# heart-rate.py
# prototype heart-rate tracker for fitness watch
# By: Tony Huang
# Created 5/5/2020
# Last modified 5/5/2020
# version 0.3


def int_input(message):
    """Gets integer input and checks it for validity before returning it"""
    #  This loop will repeat untill return() is completed sucsessfully and exits out of the function
    while True:
        try:
            return(int(input(message)))  # Prompt displayed by input() will be the paramater of the function

        except:
            print("invalid response please try again")


def resting_rate():
    """Gets input on users heart rates and calculate reserve rate"""

    resting_rate = int_input("What is your resting heart rate in bpm?: ")
    max_rate = int_input("What is your maximum heart rate in bpm?: ")

    #Returns heart rate range between resting and maximum
    return(max_rate - resting_rate)



def intensity():
    """Determins intensity of exercise based of heart_rate input"""


def exercise_selector():
    """Allows user to select the exercise they are performing"""


def output():
    """Disaplays completed exercise, length of time, and intensity"""


def main():
    """Main sequence"""

