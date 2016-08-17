# Simple Text Adventure Skeleton Code for Python

import sys

class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def print_inventory(self):
        print "Inventory: {}".format(self.inventory.keys())

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def remove_item(self, item):
        self.items.pop(item)

def print_title_screen():
    print "+------------------------------------------------+"
    print "| Simple Text Adventure Skeleton Code for Python |"
    print "+------------------------------------------------+"
    print

def move(userinput, rooms, x, y):
    nogo = "You can't go that way."
    if userinput == "n":
        if y > 0: y -= 1
        else: print nogo
    elif userinput == "s":
        if y < map_height - 1: y += 1
        else: print nogo
    elif userinput == "e":
        if x > 0: x -= 1
        else: print nogo
    elif userinput == "w":
        if x < map_width - 1: x += 1
        else: print nogo
    return x, y

def get(inventory, item, tuple, room):
    if item in room.items:
        tuple = {item: room.items[item]}
        inventory.update(tuple)
        print "You pick up the {}.".format(item)
        room.remove_item(item)
    else:
        print "You don't see that here."

def printlocation(room):
    print room.name + ": " + room.description

def printroomitems(room):
    if len(room.items.keys()) > 0:
        print "You see: {}".format(room.items.keys())
    else:
        print "You see nothing of interest."

def getuserinput():
    userinput = raw_input("> ")
    userinput = userinput.split()
    command = ""
    if len(userinput) > 0:
        command = userinput[0]
    item = ""
    if len(userinput) > 1:
        item = userinput[1]
    return command, item

def computeuserinput(command, commands, directions, room, item, x, y, nosee, nounderstand, gamehelp):
    if command in directions:
        x, y = move(command, world, x, y)
        printlocation(room)
        printroomitems(room)
    elif command == "look":
        if command == "look":
            printlocation(room)
            printroomitems(room)
        elif item in room.items:
            print room.items[userinput[5:]]
        elif item in player.inventory:
            print player.inventory[userinput[5:]]
        else:
            print nosee
    elif command == "get":
        get(player.inventory, item, tuple, room)
    elif command == "i":
        player.print_inventory()
    elif command == "help":
        print gamehelp
    elif command == "quit":
        print "Goodbye."
        sys.exit()
    else:
        print nounderstand

# Build rooms (ideally room and item details should be parsed from a separate data file)
map_width, map_height = 2, 2
world = [[Room("", "", "") for x in range(map_width)] for y in range(map_height)]
world[0][0] = Room("Bedroom", "You are in your bedroom.", {"wallet": "Your wallet is empty.", "keys": "The key ring holds a house key and a car key."})
world[0][1] = Room("Bathroom", "You step into the bathroom.", {"magazine": "Tentacle's Health: Top 10 Ways to Buff Your Suckers", "toilet paper": "You never know when you might need it."})
world[1][0] = Room("Kitchen", "You have fond memories of your mother cooking meals here.", {"apple": "It's a Fuji apple.", "chainsaw": "The perfect tool for cutting down trees and dismembering bodies."})
world[1][1] = Room("Garage", "You are now standing in the garage.", {"car": "The light glistens off the layer of dust on your 1989 Honda Civic hatchback.", "gasoline": "The gas can is red."})

# Define parameters
x, y = 0, 0
room = world[x][y]
directions = ["n", "e", "s", "w"]
commands = ["look", "get", "i", "help", "quit"]
nosee = "You don't see that here."
nounderstand = "I don't understand."
gamehelp = "Type n/e/s/w to move your player\nType i to view your inventory\nType get + the item to pick up an item\nType quit to quit the game"

print_title_screen()

# Create player
name = raw_input("Please enter your name: ")
inventory = {}
player = Player(name, inventory)
print "Hello, {}.".format(player.name)

# Game loop
printlocation(room)
printroomitems(room)
while True:
    command, item = getuserinput()
    computeuserinput(command, commands, directions, room, item, x, y, nosee, nounderstand, gamehelp)
    
