from room import Room
from player import Player
from item import Item
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

def try_move(player, direction):
    attr = direction + '_to'
    if hasattr(player.location, attr):
        player.location = getattr(player.location, attr)
    else:
        print('Nothing in that direction!\n')

def generate_room_items(items):
    for item in items:
        items[item].is_in_room = False
    
    numbers = random.sample(range(1, 9), 3)
    items[int(numbers[0])].is_in_room = True
    items[int(numbers[1])].is_in_room = True
    items[int(numbers[2])].is_in_room = True

    print(f"Items in this room are: {items[int(numbers[0])]}, {items[int(numbers[1])]}, and {items[int(numbers[2])]}")

items = {
    1 : Item(1, 'Lantern', False),
    2 : Item(2, 'Watch', False),
    3 : Item(3, 'Note', False),
    4 : Item(4, 'Thimble', False),
    5 : Item(5, 'Key', False),
    6 : Item(6, 'Lighter', False),
    7 : Item(7, 'Stick', False),
    8 : Item(8, 'Monacle', False),
    9 : Item(9, 'Hat', False)
}

# Make a new player object that is currently in the 'outside' room.

player = Player('test', room['outside'], [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
userPlaying = True
valid_command = False

while userPlaying:
    print(player.location)
    generate_room_items(items)
    valid_command = False

    while not valid_command:
        # get user input
        command = input('\nWhat do you want to do?: ').strip().lower().split()
        first_letter = command[0]
        first_first_letter = first_letter[0]

        # REPL parser

        # handling player wanting to alt-f4
        if first_first_letter == 'q':
            userPlaying = False

        # handling item pickup
        if command[0] == 'get':
            # check if the item is in that room
            if len(command) == 2:
                for key, value in items.items():
                    if value.item_name.lower() == command[1]:
                        if value.is_in_room:
                            player.items.append(value.item_name)
                            print(f'Item: {value.item_name} added to inventory')
                        else:
                            print(f"That item isn't in the room!")
            else:
                print('Please specify the item you want to pick up (ex: get [item_name])\n')
                continue
        
        # handling movement commands
        if first_first_letter == 'n':
            try_move(player, first_first_letter)
        elif first_first_letter == 's':
            try_move(player, first_first_letter)
        elif first_first_letter == 'e':
            try_move(player, first_first_letter)
        elif first_first_letter == 'w':
            try_move(player, first_first_letter)
        else:
            print('\nNot a valid command!')