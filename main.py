destinations = ["Tokyo", "Boston", "Paris"]
restaurants = ["Chicken", "Burgers", "Turkey Spot"]
modes_of_transportation = ["Rental Car", "Train", "Plane"]
entertainments = ["Karoake", "Touring Ellis Island", "Movies"]

import random

print("Welcome to the Day Trip Generator, if you're not sure what you would like to do for your trip you have come to the right place!")


def choose_destination():
    destination_one = random.choice(destinations)
    print(f"We have selected {destination_one} for your destination! Does this sound good? Enter y/n:")
    destinations.remove(destination_one)
    user_input = input()
    if user_input == "n":
        destination_two = random.choice(destinations)
        print(f"Oh, sorry you don't like this destination. No worries, we can try something else! How about {destination_two}? Enter y/n:")
        destinations.remove(destination_two)
        user_input_two = input()
        if user_input_two == "n":
            print(f"Oh, sorry you dont like this destination. No worries, we can try something else! There is also {destinations[0]}? Enter y/n:")
            user_input_three = input()

choose_destination()
        