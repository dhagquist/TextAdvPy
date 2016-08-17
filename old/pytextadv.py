# Simple Text Adventure Skeleton Code for Python

class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def remove_item(self, item):
        self.items.remove(item)

# Print title screen
print "+------------------------------------------------+"
print "| Simple Text Adventure Skeleton Code for Python |"
print "+------------------------------------------------+"
print

# Build player
name = raw_input("Please enter your name: ")
inventory = []
player = Player(name, inventory)
print "Hello, {}.".format(player.name)

# Build rooms and load into map
map_width, map_height = 2, 2
world = [[Room("", "", "") for x in range(map_width)] for y in range(map_height)]
world[0][0] = Room("Bedroom", "You are in your bedroom.", ["wallet", "keys"])
world[0][1] = Room("Bathroom", "You are in the bathroom.", ["magazine", "toilet paper"])
world[1][0] = Room("Kitchen", "You are in the kitchen.", ["apple", "chainsaw"])
world[1][1] = Room("Garage", "You are in the garage", ["car", "gasoline"])

def move(userinput, rooms, x, y):
    if userinput == "n":
        if y > 0: y -= 1
        else: print "You can't go that way."
    elif userinput == "s":
        if y < map_height - 1: y += 1
        else: print "You can't go that way."
    elif userinput == "e":
        if x > 0: x -= 1
        else: print "You can't go that way."
    elif userinput == "w":
        if x < map_width - 1: x += 1
        else: print "You can't go that way."
    return x, y

def get(inventory, item, room):
    if item in room.items:
        inventory.append(item)
        print "You pick up the {}.".format(item)
        room.remove_item(item)
    else:
        print "You don't see that here."

# Game loop
x, y = 0, 0
print world[x][y].name + ": " + world[x][y].description
print "You see: {}".format(world[x][y].items)
while True:
    userinput = raw_input("> ")
    if userinput in ["n", "e", "s", "w"]:
        x, y = move(userinput, world, x, y)
        print world[x][y].name + ": " + world[x][y].description
        print "You see: " + str(world[x][y].items)
    elif userinput == "look":
        print world[x][y].name + ": " + world[x][y].description
        print "You see: " + str(world[x][y].items)
    elif userinput[:4] == "get ":
        item = userinput[4:]
        get(player.inventory, item, world[x][y])
    elif userinput == "i":
        print "Inventory: {}".format(player.inventory)
    elif userinput == "help":
        print "Type n/e/s/w to move your player"
        print "Type i to view your inventory"
        print "Type get + the item to pick up an item"
        print "Type quit to quit the game"
    elif userinput == "quit":
        break
    else: print "I don't understand."
