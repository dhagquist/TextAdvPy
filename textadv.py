# Text Adventure

# TO DO:
# -add drop support for inventory items
# -pretty print for room items and inventory

import sys
import string

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
    def removeitem(self, item):
        self.items.pop(item)
    def printlocation(self):
        print self.name + ": " + self.description
    def printitems(self):
        if len(self.items.keys()) > 0:
            print "You see: {}".format(self.items.keys())
        else:
            print "You see nothing of interest."

def titlescreen():
    print "+---------------------------+"
    print "| Text Adventure for Python |"
    print "+---------------------------+"
    print

def getuserinput():
    # Issue: "look keys, wallet" --> "Your wallet is empty."
    #   Assume user error, or add check?
    command = ""
    item = ""
    itemlist = []
    removewords = ["at", "the", "to"]
    userinput = raw_input("> ").lower()
    userinput = userinput.strip()
    # Command + Item processing
    # Get the command
    if len(userinput.split()) > 1:
        command = userinput[:userinput.index(" ")]
        command = command.translate(None, string.punctuation)
        command.strip()
        # Get everything after the command
        rest = userinput[userinput.index(" ") + 1:]
        rest = rest.strip()
        # Process multiple items for get command (e.g. get keys, wallet)
        # Should this be in the get function?
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
    # Test: check captured command and items
    print "Command: " + command
    print "Items: " + str(itemlist)
    return command, itemlist, item

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
    print "x: " + str(x)
    print "y: " + str(y)
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

def drop():
    # To do
    print

def savegame(x, y, inventory, name):
    import pickle
    xtemp, ytemp, i = 0, 0, 0
    roomlist = []
    for i in range(map_width - 1):
        roomlist.append(world[xtemp][ytemp])
        xtemp += 1
        for j in range(map_height - 1):
            roomlist.append(world[xtemp][ytemp])
            ytemp +=1
    print roomlist
    data = {"x": x, "y": y, "name": name, "inventory": inventory, "rooms": roomlist}
    filehandler = open("savedgame.txt","wb")
    pickle.dump(data, filehandler)
    filehandler.close()
    print "Save successful."

def loadgame():
    # Issue: JSON parses strings in unicode, so a "u" will appear before loaded inventory items
    #   Possible work-around: use a pretty print method for printing inventory and room items
    # Issue: if save, then get item, then load, item disappears (not in inv, but taken from room)
    #   Need to save room states
    #    Create list of variables to load data into, use for loop to iterate through?
    import os.path
    import pickle
    if os.path.isfile("savedgame.txt"):
        loadfile = open("savedgame.txt",'rb')
        data = pickle.load(file)
        file.close()
        global x
        global y
        x = data2["x"]
        y = data2["y"]
        name = data2["name"]
        inventory = data2["inventory"]
        print inventory
        print str(inventory)
        global Player
        player = Player(name, inventory)
        print "Load successful.\n"
        room = world[x][y]
        room.printlocation()
        room.printitems()
        print
        game(world, room, x, y, player, commands, directions, gamehelp)
    else:
        print "No saved game exists."
        

# Build rooms, load into map
# TO DO:
# -Add states and actions to rooms, e.g. open window
# -Keep all data in separate file (YAML?)
map_width, map_height = 2, 2
world = [[Room("", "", "") for n in range(map_width)] for m in range(map_height)]
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
commands = ["look", "get", "open", "close", "i", "help", "load", "save", "quit", "exit"]
gamehelp = """
Type n/e/s/w to move your player
Type i to view your inventory 
Type get + the item to pick up an item
Type get + multiple items separated by commas
Type quit to quit the game
"""

# Print title screen
titlescreen()

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
            elif command == "i":
                player.printinventory()
            elif command == "help":
                print gamehelp
            elif command == "load":
                loadgame()
            elif command == "save":
                savegame(x, y, player.inventory, player.name)
            elif command == "quit":
                print "Goodbye.\n"
                sys.exit()
        elif command == "":
            print "Cat got your tongue?"
        else:
            print "I don't understand."
        print

def menu():
    # New game / Load game
    # Note: load game currently in development
    userinput = raw_input("(N)ew Game or (L)oad Game? ").lower()
    while True:
        if userinput == "n":
            # Create player
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
            loadgame()
            break
        else:
            print "Invalid input."
            userinput = raw_input("(N)ew Game or (L)oad Game? ").lower()

# Start game
menu()
