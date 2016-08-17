# Text Adventure Skeleton Code for Python v1.0, 7/1/2016, Daniel Hagquist

class Player:
    def __init__(self, name, inventory, health, score, weapon):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.score = score
        self.weapon = weapon
    def add_inventory(self, item):
        self.inventory += items
    def print_inventory(self):
        list = []
        for item in self.inventory:
            list.append(item.name)
        print "Inventory: " + str(list)
    def add_score(self, score):
        self.score += score
    def add_health(self, health):
        self.health += health
    def subtract_health(self, health):
        self.health -= health
    def equip_weapon(self, weapon):
        self.weapon = weapon

class Room:
    def __init__(self, id, name, description, items, objects, exists, exits):
        self.id = id
        self.name = name
        self.description = description
        self.items = items
        self.objects = objects
        self.exists = exists
        self.exits = exits
    def print_room(self):
        print self.name + ": " + self.description
    def print_room_items(self, items):
        list = []
        for item in self.items:
            list.append(item.name)
        print list

# Objects that can be added to inventory, used, and acted on, e.g. a book
class Item:
    def __ini__(self, id, name, description, actions, weapon, food, canpickup):
        self.id = id
        self.name = name
        self.description = description
        self.actions = actions
        self.weapon = weapon
        self.food = food
        self.canpickup = canpickup

# Objects that can be acted on but not added to inventory, e.g. a car
class Objects:
    def __ini__(self, id, name, description, actions):
        self.id = id
        self.name = name
        self.description = description
        self.actions = actions

class Weapons:
    def __ini__(self, id, name, description, power, quality):
        self.id = id
        self.name = name
        self.description = description
        self.power = power
        self.quality = quality


def title():
    print "+---------------------------------------+"
    print "| Text Adventure Skeleton Code (Python) |"
    print "+---------------------------------------+"
    print

def buildPlayer():
    # Build player
    player = Player()
    userinput = raw_input("Please enter your name: ")
    player.set_name(userinput)
    print "Hello, " + player.name + ".\n"



title()
buildPlayer()


# Build rooms, room items, and map
map_width, map_height = 3, 3
rooms = [[Room() for x in range(map_width)] for y in range(map_height)]

# Room 1: Bedroom
rooms[0][0].set_name("Bedroom")
rooms[0][0].set_description("You are standing in your bedroom.")
wallet = Item()
wallet.set_name("wallet")
wallet.set_description("Your wallet is empty.")
# wallet.set_actions(["look", "open", "close"])
keys = Item()
keys.set_name("keys")
keys.set_description("The key is old and rusty.")
# keys.set_actions(["look", "use"])
rooms[0][0].add_items([wallet, keys])


print "Test ------"
roomtest = Room2("Bedroom", "You are standing in your bedroom.", [wallet, keys], True, ["n", "s"])
roomtest.print_room()
roomtest.print_room_items(roomtest.items)
print "-------"



rooms[0][1].set_name("Bathroom")
rooms[0][1].set_description("You are in the bathroom.")
rooms[0][1].add_items(["toilet paper", "magazine"])


rooms[1][0].set_name("Kitchen")
rooms[1][0].set_description("You are in the kitchen.")
rooms[1][0].add_items(["towel", "chainsaw"])


rooms[1][1].set_name("Garage")
rooms[1][1].set_description("You are in the garage.")
rooms[1][1].add_items(["car", "gasoline"])

def move(userinput, rooms, x, y):
    if userinput == "n":
        if y > 0:
            y -= 1
        else: print "You can't go that way."
    elif userinput == "s":
        if y < map_height - 1:
            y += 1
        else: print "You can't go that way."
    elif userinput == "e":
        if x > 0:
            x -= 1
        else: print "You can't go that way."
    elif userinput == "w":
        if x < map_width - 1:
            x += 1
        else: print "You can't go that way."
    return x, y

def get(inventory, checkitem, room):
    for item in room.items:
        if item.name == checkitem:
            inventory.append(item)
            room.remove_item(item)
            print "You pick up the " + item.name + "."
            break
        else:
            print "You don't see that here."

x, y = 0, 0
print rooms[x][y].name
playing = True
while playing:
    userinput = raw_input("> ")
    if userinput in ['n', 's', 'e', 'w']:
        x, y = move(userinput, rooms, x, y)
        print rooms[x][y].name
    elif userinput == "look":
        print rooms[x][y].description
        rooms[x][y].print_items()
    elif userinput[:4] == "get ":
        item = userinput[4:]
        get(player.inventory, item, rooms[x][y])
    elif userinput == "i":
        player.print_inventory()
    elif userinput == "help":
        print "Type n/e/s/w to move your player"
        print "Type i to view your inventory"
        print "Type me to view your player status"
        print "Type quit to quit the game"
        print "Other commands: get, look, open, close, and more."
    elif userinput == "me":
        print "Name: " + player.name
        print "Health: " + str(player.health)
        print "Score: " + str(player.score)
        print "Inventory: " + str(player.inventory)
        print "Weapon: " + player.weapon
    elif userinput == "quit":
        playing = False
    else: print "I don't understand."
