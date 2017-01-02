'''
Text Adventure for Python 2.7

A simple, work-in-progress, free and open source text adventure
for beginners and hobbyists.

Last updated 1/1/2017
-Added save/load game functionality
-Added functionality for drop
-Cleaned up code a bit

TO DO:
------
-Keep text for rooms, descriptions, commands, etc. in a separate file (JSON, YAML, etc.)
-Add states and actions to rooms, e.g. open/close window
-Pretty print for room items and inventory
-"look keys, wallet" --> "Your wallet is empty.". Assume user error, or add check?
-Add support for multiple item drop?
'''

import sys
import string
import pickle

class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def printinventory(self):
        print "Inventory: {}".format(self.inventory.keys())

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def additem(self, item):
        self.items.push(item)
    def removeitem(self, item):
        self.items.pop(item)
    def printlocation(self):
        print self.name + ": " + self.description
    def printitems(self):
        if len(self.items.keys()) > 0:
            print "You see: {}".format(self.items.keys())
        else:
            print "You see nothing of interest."

def getuserinput():
    command = ""
    item = ""
    itemlist = []
    removewords = ["at", "the", "to"]
    userinput = raw_input("> ").lower()
    userinput = userinput.strip()
    # Get the command
    if len(userinput.split()) > 1:
        command = userinput[:userinput.index(" ")]
        command = command.translate(None, string.punctuation)
        command.strip()
        # Get everything after the command
        rest = userinput[userinput.index(" ") + 1:]
        rest = rest.strip()
        # Check if multiple items for get command (e.g. get keys, wallet)
        if "," in rest:
            rest = rest.split(",")
            for item in rest:
                item = item.translate(None, string.punctuation)
                item = item.strip()
                itemlist.append(item)
        # Otherwise it's a two-word single item (e.g. toilet paper)
        else:
            rest.strip()
            itemlist.append(rest)
    # Single word commands
    else:
        command = userinput.strip()
        command = command.translate(None, string.punctuation)
    # Single item as string for flexibility in processing
    if len(itemlist) == 1:
        item = itemlist[0]
    # Remove extraneous words (e.g. "at", "the", "to")
    itemlist = [word for word in itemlist if word not in removewords]
    return command, itemlist, item

def move(command, x, y):
    nogo = "You can't go that way."
    if command == "n":
        if y > 0: y -= 1
        else: print nogo
    elif command == "s":
        if y < MAP_HEIGHT - 1: y += 1
        else: print nogo
    elif command == "e":
        if x > 0: x -= 1
        else: print nogo
    elif command == "w":
        if x < MAP_WIDTH - 1: x += 1
        else: print nogo
    return x, y

def get(inventory, item, itemlist, room):
    if len(itemlist) == 0:
        print "Get what?"
    for item in itemlist:
        if item in room.items:
            tuple = {item: room.items[item]}
            inventory.update(tuple)
            room.removeitem(item)
            print "You pick up the {}.".format(item)
        else:
            print "You don't see that here."

def drop(inventory, item, itemlist, room):
    if item in inventory:
        tuple = {item: inventory[item]}
        inventory.pop(item)
        room.items.update(tuple)
        print "You drop the " + str(item) + "."
    else:
        print "You don't have that."

def savegame(x, y, player, world, room):
    with open('savedgame.pkl', 'w') as f:
        pickle.dump([player, world, room, x, y], f)
        print "Save successful."

def loadgame(world, room, x, y, player, commands, directions, gamehelp):
    with open('savedgame.pkl') as f:
        player, world, room, x, y = pickle.load(f)
        print "Load successful."
        game(world, room, x, y, player, commands, directions, gamehelp)

def titlescreen():
    print "+---------------------------+"
    print "| Text Adventure for Python |"
    print "+---------------------------+"

# Create world/map, initialize and build rooms inside of map 
MAP_WIDTH, MAP_HEIGHT = 2, 2
world = [[Room("", "", "") for n in range(MAP_WIDTH)] for m in range(MAP_HEIGHT)]
world[0][0] = Room("Bedroom", "You are in your childhood bedroom.",
                   {"wallet": "Your wallet is empty. Are you surprised?",
                    "keys": "The key ring holds a house key and a car key."})
world[0][1] = Room("Bathroom", "You step into the bathroom.",
                   {"magazine": "Tentacle's Health: Top 10 Ways to Buff Your Suckers",
                    "toilet paper": "You never know when you might need it."})
world[1][0] = Room("Kitchen", "You have fond memories of your mother cooking meals here.",
                   {"apple": "It's a Fuji apple.",
                    "chainsaw": "The perfect tool for cutting down trees and dismembering bodies."})
world[1][1] = Room("Garage", "You are now standing in the garage.",
                   {"car": "The light glistens off the layer of dust on your 1989 Honda Civic hatchback.",
                    "gasoline": "The gas can is red."})

# Set up game parameters
x, y = 0, 0
room = world[x][y]
directions = ["n", "e", "s", "w"]
commands = ["look", "get", "drop", "open", "close", "i", "help", "load", "save", "quit", "exit"]
gamehelp = """
Instructions:
Type n/e/s/w to move your player
Type i to view your inventory 
Type get + the item to pick up an item
Type get + multiple items separated by commas
Type quit to quit the game
Some common commands:
look, get, open, close, load, save, help, quit
"""

titlescreen()
print gamehelp

def game(world, room, x, y, player, commands, directions, gamehelp):
    while True:
        command, itemlist, item = getuserinput()
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
                get(player.inventory, item, itemlist, room)
            elif command == "drop":
                drop(player.inventory, item, itemlist, room)
            elif command == "i":
                player.printinventory()
            elif command == "help":
                print gamehelp
            elif command == "load":
                loadgame(world, room, x, y, player, commands, directions, gamehelp)
            elif command == "save":
                savegame(x, y, player, world, room)
            elif command == "quit":
                print "Goodbye.\n"
                sys.exit()
        elif command == "":
            print "Cat got your tongue?"
        else:
            print "I don't understand."
        print

def menu():
    userinput = raw_input("(N)ew Game or (L)oad Game? ").lower()
    while True:
        if userinput == "n":
            name = raw_input("\nPlease enter your name: ")
            inventory = {}
            global player
            player = Player(name, inventory)
            print "Hello, {}.\n".format(player.name)
            room.printlocation()
            room.printitems()
            print
            game(world, room, x, y, player, commands, directions, gamehelp)
            break
        elif userinput =="l":
            global player
            player = Player("", {})
            loadgame(world, room, x, y, player, commands, directions, gamehelp)
            break
        else:
            print "Invalid input."
            userinput = raw_input("(N)ew Game or (L)oad Game? ").lower()

if __name__ == "__main__":
    menu()
