destinations = ["Tokyo", "Boston", "Paris"]
restaurants = ["Chicken", "Burgers", "Turkey Spot"]
transportations = ["Rental Car", "Train", "Plane"]
entertainments = ["Karoake", "Touring Ellis Island", "Movies"]

import random
from turtle import goto

print("Welcome to the Day Trip Generator, if you're not sure what you would like to do for your trip you have come to the right place!")


def choose_destination():
    destination_one = random.choice(destinations)
    print(f"We have selected {destination_one} for your destination! Does this sound good? Enter y/n:")
    destinations.remove(destination_one)
    result_one = destination_one
    user_input = input()
    if user_input == "n":
        destination_two = random.choice(destinations)
        print(f"Oh, sorry you don't like this destination. No worries, we can try something else! How about {destination_two}? Enter y/n:")
        destinations.remove(destination_two)
        result_one = destination_two
        user_input_two = input()
        if user_input_two == "n":
            print(f"Oh, sorry you dont like this destination. No worries, we can try something else! There is also {destinations[0]}? Enter y/n:")
            user_input_three = input()
            result_one = destinations[0]
        else:
             user_input_three   
            
            
    return result_one   

     
choice_destination = choose_destination()


print("Awesome! Glad that is decided. Let's move on!")

def choose_restaurant():
    restaurant_one = random.choice(restaurants)
    print(f"We have selected {restaurant_one} for your restaurant! Does this sound good? Enter y/n:")
    restaurants.remove(restaurant_one)
    result_two = restaurant_one
    user_input = input()
    if user_input == "n":
        restaurant_two = random.choice(restaurants)
        print(f"Oh, sorry you don't like this restaurant. No worries, we can try something else! How about {restaurant_two}? Enter y/n:")
        destinations.remove(restaurant_two)
        result_two = result_two
        user_input_two = input()
        if user_input_two == "n":
            print(f"Oh, sorry you dont like this restaurant. No worries, we can try something else! There is also {restaurants[0]}? Enter y/n:")
            user_input_three = input()
            result_two = restaurants[0]
        else:
            user_input_three
            

    return result_two       
choice_restaurant = choose_restaurant()

print("Awesome! Glad that is decided. Let's move on!")

def choose_transportation():
    transportation_one = random.choice(transportations)
    print(f"We have selected {transportation_one} for your transportation! Does this sound good? Enter y/n:")
    transportations.remove(transportation_one)
    result_three = transportation_one
    user_input = input()
    if user_input == "n":
        transportation_two = random.choice(destinations)
        print(f"Oh, sorry you don't like this transportation. No worries, we can try something else! How about {transportation_two}? Enter y/n:")
        destinations.remove(transportation_two)
        result_three = transportation_two
        user_input_two = input()
        if user_input_two == "n":
            print(f"Oh, sorry you dont like this transportation. No worries, we can try something else! There is also {transportations[0]}? Enter y/n:")
            result_three = transportations[0]
            user_input_three = input()
        else:
            user_input_three
            
    return result_three
choice_transportation = choose_transportation()

print("Awesome! Glad that is decided. Let's move on!")

def choose_entertainment():
    entertainment_one = random.choice(entertainments)
    print(f"We have selected {entertainment_one} for your entertainment! Does this sound good? Enter y/n:")
    entertainments.remove(entertainment_one)
    result_four = entertainment_one
    user_input = input()
    if user_input == "n":
        entertainment_two = random.choice(entertainments)
        print(f"Oh, sorry you don't like this entertainment. No worries, we can try something else! How about {entertainment_two}? Enter y/n:")
        destinations.remove(entertainment_two)
        result_four = entertainment_two
        user_input_two = input()
        if user_input_two == "n":
            print(f"Oh, sorry you dont like this entertainment. No worries, we can try something else! There is also {entertainments[0]}? Enter y/n:")
            result_four = entertainments[0]
            user_input_three = input()
        else:
            user_input_three
            
    return result_four
choice_entertainment = choose_entertainment()

print("Awesome! Glad that is decided. Let's move on!")

print("Congrats! We have completed generating your day trip. Now let's just confirm that this is the trip you wanted")

print("The trip we have generated for you is: ")
print(f"Destination: {choice_destination}")
print(f"Restaurant: {choice_restaurant}")
print(f"Transportation: {choice_transportation}")
print(f"Entertainment: {choice_entertainment}")


print(f"Would you like to finalize this trip? Enter y/n: {input()}")

if input() == "y":
    print(f"Prepare for your dream vacation to come alive! You will be arriving in {choice_destination} by {choice_transportation}, where you will spend the day in {choice_entertainment}.  You will end the evening dining in style at {choice_restaurant}, a famous local restaurant.")
