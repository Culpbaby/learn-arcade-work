"""Lab 4 Skybison"""

import random


# Main Function

def main():
    miles_traveled = 0
    thirst = 0
    skybison_tiredness = 0
    airnation_natives_distance_traveled = -20
    drinks_in_pouch = 4

    print("Welcome to Skybison!")
    print("You have stolen a Skybison to make your way to Bai Sing Se.")
    print("The Air-nation wants their Skybison back and are chasing you down! Survive your")
    print("desert trek and out run the Air-nation.")
    print(" ")

    done = False

    while not done:
        print("A. Drink from your pouch.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print("     ")

# If quitting

        choice = input("What is your choice? ")
        if choice.lower() == "q":
            print("   ")
            print("You have quit and the Air-nation have taken you prisoner.")
            done = True
    #status check
        elif choice.lower() == "e":
            print("   ")
            print("Miles traveled:", end=" ")
            print(miles_traveled)
            print("Drinks left in pouch:", end=" ")
            print(drinks_in_pouch)
            print("The Air-nation is:", end=" ")
            print(miles_traveled - airnation_natives_distance_traveled, end=" ")
            print("miles behind you!")
            print("  ")

        #Stopping for the night
        elif choice.lower() == "d":
            skybison_tiredness = 0
            print(" ")
            print("Your skybison is very happy")
            airnation_natives_distance_traveled += random.randrange(9, 22)
            print("The Air-nation is", end=" ")
            print(miles_traveled - airnation_natives_distance_traveled, end=" ")
            print("miles behind you!")
            print("  ")

        #Ahead full speed.
        elif choice.lower() == "c":
            miles_traveled += random.randrange(13, 27)
            thirst += 1
            skybison_tiredness += random.randrange(1,3)
            airnation_natives_distance_traveled += random.randrange(7, 15)
            print(" ")
            print("You have traveled", end=" ")
            print(miles_traveled, end=" ")
            print("miles")
            print(" ")
            if random.randrange(0, 21) == 13:
                    print(" ")
                    print("You have found an Oasis!")
                    print(" ")
                    drinks_in_pouch = 4
                    thirst = 0
                    skybison_tiredness = 0


        #Ahead moderate speed.
        elif choice.lower() == "b":
            miles_traveled += random.randrange(5, 13)
            thirst += 1
            skybison_tiredness += 1
            airnation_natives_distance_traveled += random.randrange(7, 15)
            print(" ")
            print("You have traveled", end=" ")
            print(miles_traveled, end=" ")
            print("miles")
            print(" ")
            if random.randrange(0, 21) == 13:
                print(" ")
                print("You have found an Oasis!")
                print(" ")
                drinks_in_pouch = 4
                thirst = 0
                skybison_tiredness = 0
# drink from pouch
        elif choice.lower() == "a":
            drinks_in_pouch -= 1
            thirst = 0
            airnation_natives_distance_traveled += random.randrange(2, 5)
            print(" ")
            print("Drinks left in your pouch,", end=" ")
            print(drinks_in_pouch, ".")
            print(" ")
        if thirst > 4:
            print(" ")
            print("You are thirsty")
            print(" ")
        elif thirst > 6:
            print(" ")
            print("You died of thirst!")
            print(" ")
            done = True
        if skybison_tiredness > 4:
            print(" ")
            print("Your Skybison is getting tired.")
            print(" ")
        elif skybison_tiredness > 7:
            print(" ")
            print("Your Skybison is dead.")
            print(" ")
            done = True
        if airnation_natives_distance_traveled >= miles_traveled:
            print(" ")
            print("The Air-nation natives have caught you.")
            print("The game is over.")
            print(" ")
            done = True
        elif airnation_natives_distance_traveled >= (miles_traveled - 15):
            print(" ")
            print("The Air-nation natives are getting close!")
            print(" ")
        if miles_traveled >= 200:
            print(" ")
            print("You have made it to Ba Sing Se, and have won the game!")
            print(" ")
            done = True

main()