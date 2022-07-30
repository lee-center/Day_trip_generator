import random



fun_places_list = ["bogus basin" , "the village" , "lucky peak lake", "overland park theatre"]
eats_list = ["bad boy burgers" , "bob's sunrise cafe" , "reeds dairy" , "wagon wheel dive"]
wheels_list = ["tesla" , "ford f250" , "chevy camaro" , "Toyota Sequoia"]
towns_list = ["Boise" , "Emmett" , "Rexburg" , "Mountain Home" ]


def give_random_from_list(selected_list):
    random_item = random.choice(selected_list)
    return random_item



def welcome_message():
    # replace pass with print statment explaing the program to the user
     print("welcome to the random idaho tour selector!  I will randomly select for you popular tourist towns, good food, and something to do in every town! lets get started!")

def fun_place_picker():
    random_place = give_random_from_list(fun_places_list)
    print(f'We have selected {random_place} for your destination, is this ok? y/n')
    user_choice = input("enter selection ")
    choice_made = False 
    while choice_made == False:
        if user_choice == "y":
            print("This choice has been confirmed")
            return random_place
        elif user_choice == "n":
            random_place = give_random_from_list(fun_places_list)
            print(f'We have selected {random_place} for your destination, is this ok? y/n')
            user_choice = input("enter selection ")
            continue

def eats_picker():
    random_food = give_random_from_list(eats_list)
    print(f'we have selected {random_food} for your meal. Is that yummy enough? y/n')
    choice_made = False
    while choice_made == False:
        if user_choice == "y":
            print("good eats!")
            user_choice = input("enter selection")
            return random_food
        elif user_choice == "n":
            print(f'we have selected {random_food} for your meal.  Is that yummy enough? y/n')
            continue

def wheels_picker():
    random_car = give_random_from_list(wheels_list)
    print(f'we have selected{random_car} for your transport.  Is it slick enough? y/n')
    choice_made = False
    while choice_made == False:
        if user_choice == "y":
            print("peel the road back!")
            user_choice = ("enter selection")
            
    

def towns_picker():
    random_town = give_random_from_list(towns_list)
    print(f"we have selected{random_town} for your adventure. Are you curious?  y/n")
    choice_made = False
    while choice_made == "y":
        if user_choice == "y":
            print("tear up the town!")
            user_choice= ("enter selection")
#as you build out your functions use the confimred variable to pass in the selection the user made 
def confirm_trip(confirmed_fun_place):
    print(f'Your trip to {confirmed_fun_place}')
    user_choice = input("To confirm the trip enter Yes, to start over enter No.")
    if user_choice == "Yes":
            print("have a nice trip")
    elif user_choice == "No":
            print("lets try that again")
            controller_function()

# this will call all of our other function calls 
def controller_function():
    welcome_message()
    # need to setup the 3 other function calls like this one 
    confirmed_fun_place = fun_place_picker()



    # after setting up the above function calls you will need to pass their results 
    # into this confirm_trip function to have access to their values
    confirm_trip(confirmed_fun_place)
controller_function()
    