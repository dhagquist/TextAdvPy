# Simple Text Adventure Skeleton Code for Python
# Programmed by Daniel Hagquist

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
    def printlocation(self):
        print self.name + ": " + self.description
    def printitems(self):
        if len(self.items.keys()) > 0:
            print "You see: {}".format(self.items.keys())
        else:
            print "You see nothing of interest."

def titlescreen():
    print "+------------------------------------------------+"
    print "| Simple Text Adventure Skeleton Code for Python |"
    print "+------------------------------------------------+"
    print

def getuserinput():
    userinput = raw_input("> ").split()
    command = ""
    item = ""
    if len(userinput) == 1:
        command = userinput[0]
    elif len(userinput) == 2:
        command = userinput[0]
        item = userinput[1]
    elif len(userinput) > 2:
        print "Too many words."
    return command, item

def computecommand(command, commands, item, directions, x, y, player, room, gamehelp):
    if command in directions and len(item) == 0:
        x, y = move(command, x, y)
        room = world[x][y]
        room.printlocation()
        room.printitems()
    elif command in commands:
        if command == "look":
            if len(item) == 0:
                room.printlocation()
                room.printitems()
            elif item in room.items.keys():
                print room.items[item]
            elif item in player.inventory:
                print player.inventory[item]
            else:
                print "You don't see that here."
        elif command == "get":
            get(player.inventory, item, room)
        elif command == "i":
            player.print_inventory()
        elif command == "help":
            print gamehelp
        elif command == "quit":
            print "Goodbye."
            sys.exit()
    elif command == "":
        print "Cat got your tongue?"
    else:
        print "I don't understand."

def move(command, x, y):
    nogo = "You can't go that way."
    if command == "n":
        if y > 0: y -= 1
        else: print nogo
    elif command == "s":
        if y < map_height - 1: y += 1
        else: print nogo
    elif command == "e":
        if x > 0: x -= 1
        else: print nogo
    elif command == "w":
        if x < map_width - 1: x += 1
        else: print nogo
    return x, y

def get(inventory, item, room):
    if item in room.items:
        tuple = {item: room.items[item]}
        inventory.update(tuple)
        print "You pick up the {}.".format(item)
        room.remove_item(item)
    else:
        print "You don't see that here."

def savegame():
    print""

def loadgame():
    print""

# Build rooms, load into map (ideally room and item details should be parsed from a separate data file)
map_width, map_height = 2, 2
world = [[Room("", "", "") for x in range(map_width)] for y in range(map_height)]
world[0][0] = Room("Bedroom", "You are in your childhood bedroom.", {"wallet": "Your wallet is empty.", "keys": "The key ring holds a house key and a car key."})
world[0][1] = Room("Bathroom", "You step into the bathroom.", {"magazine": "Tentacle's Health: Top 10 Ways to Buff Your Suckers", "toilet paper": "You never know when you might need it."})
world[1][0] = Room("Kitchen", "You have fond memories of your mother cooking meals here.", {"apple": "It's a Fuji apple.", "chainsaw": "The perfect tool for cutting down trees and dismembering bodies."})
world[1][1] = Room("Garage", "You are now standing in the garage.", {"car": "The light glistens off the layer of dust on your 1989 Honda Civic hatchback.", "gasoline": "The gas can is red."})

# Set up game parameters
x, y = 0, 0
room = world[x][y]
directions = ["n", "e", "s", "w"]
commands = ["look", "get", "open", "close", "i", "help", "quit"]
gamehelp = "Type n/e/s/w to move your player\nType i to view your inventory\nType get + the item to pick up an item\nType quit to quit the game"

titlescreen()

# Create player
name = raw_input("Please enter your name: ")
inventory = {}
player = Player(name, inventory)
print "Hello, {}.\n".format(player.name)

# Start game loop
room.printlocation()
room.printitems()
print
while True:
    command, item = getuserinput()
    computecommand(command, commands, item, directions, x, y, player, room, gamehelp)
    print
