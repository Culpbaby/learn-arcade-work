# Lab 6 Text Adventure

class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    # Room 0 or kitchen.
    room_list = []
    room = Room("""You have entered the apartment and are now in the Kitchen,
There is a door to the south.""", north = None, east = None, south = 1, west = None)
    room_list.append(room)

    # Room 1 or living room.
    room_1 = Room("""You have now entered the living room!
There are three doors here, a north door, east door, 
and a south door.""", north = 0, east = 2, south = 5, west = None)
    room_list.append(room_1)

    # Room 2 or bedroom 2
    room_2 = Room("""You have entered your friend's roommates's bedroom. Luckily his 
    roommate is really cool and will let you travel through. 
    Their is a door to the north and another on to the east.""", north=3, east=6, south=None, west=1)
    room_list.append(room_2)

    # Room 3 or Bathroom 3
    room_3 = Room("""You have entered your friends bathroom.
    The only door is to the south and it smells bad in 
    the bathroom.""", north=None, east=None, south=2, west=None)
    room_list.append(room_3)

    # Room 4 or bathroom 4
    room_4 = Room("""You have entered your friend's bathroom. 
    Your friend is also not in here. There is a door to the north.""", north=6, east=None, south=None, west=None)
    room_list.append(room_4)

    # Room 5 or backyard.
    room_5 = Room("""You have excited the house and are now in the backyard.
you may go head back inside through the door to the north""", north = 1, east = None, south = None, west = None)
    room_list.append(room_5)

    # Room 6 or bedroom 6
    room_6 = Room("""You have entered your friend's bedroom. They seem 
to not be in here. There is a door to the south and a 
door to the west.""", north = None, east = None, south = 4, west = 2)
    room_list.append(room_6)



    current_room = 0

    done = False

    while done != True:
        print()
        print(room_list[current_room].description)
        choice = input("What do you want to do? ")

        if choice.lower() == "n" or choice.lower() == "north" or choice.lower() == "go north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif choice.lower() == "e" or choice.lower() == "east" or choice.lower() == "go east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif choice.lower() == "s" or choice.lower() == "south" or choice.lower() == "go south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif choice.lower() == "w" or choice.lower() == "west" or choice.lower() == "go west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif choice.lower() == "q" or choice.lower() == "quit":
            print("You have quit the game. Goodbye.")
            done = True

        else:
            print("What? That wasn't on option. Please try something else.")

main()