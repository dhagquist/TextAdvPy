def title():
    print "+---------------------------------------+"
    print "| Text Adventure Skeleton Code (Python) |"
    print "+---------------------------------------+"
    print

class Player:
    def __init__(self, name, status, inventory):
        self.name = name
        self.status = status
        self.inventory = inventory
    def add_inventory(self, item):
        self.inventory += items
    def print_inventory(self):
        list = []
        for item in self.inventory:
            list.append(item.name)
        print "Inventory: " + str(list)

class Room:
    def __init__(self, id, name, description, items, objects):
        self.id = id
        self.name = name
        self.description = description
        self.items = items
        self.objects = objects
    def print_room(self):
        print self.name + ": " + self.description
    def print_room_items(self):
        list = []
        for item in self.items:
            list.append(item.name)
        if len(list) > 0:
            print "Items: {}".format(list)
    def print_room_objects(self):
        list = []
        for object in self.objects:
            list.append(object.name)
        if len(list) > 0:
            print "Interactive objects: {}".format(list)

class Item:
    def __init__(self, id, name, description, status, actions, isFood, canPickUp):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.actions = actions
        self.isFood = isFood
        self.canPickUp = canPickUp

class Object:
    def __init__(self, id, name, description, status, actions):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.actions = actions

def buildPlayer():
    # name = raw_input("Please enter your name: ")
    name = "Dan"
    status = "You are ready to embark on your adventure."
    inventory = []
    player = Player(name, status, inventory)
    print "Hello, " + player.name + ".\n"
    return player
    
def buildBedroom():

    id = 1
    name = "Bedroom"
    description = "This is your childhood bedroom."

    # Create Item objects to be added to room object
    # id, name, description, status, actions, isFood, canPickUp
    walletHasLicense = False
    wallet = Item(1, "Wallet", "Your wallet is made of the finest of faux leather.",
                  walletHasLicense, ["open", "close"],
                  False, True)
    keyUsed = False
    key = Item(2, "Key", "A single key with which you are unfamiliar.",
                  keyUsed, ["use", "unlock"],
                  False, True)
    items = [wallet, key]

    # Create Object objects to be added to room object
    # id, name, description, status, actions
    messyBed = True
    bed = Object(1, "bed", "Your bed is very messy.", messyBed, ["make bed"])
    fanOff = True
    fan = Object(2, "ceiling fan", "The fan hasn't been cleaned in years.", fanOff,
                 ["turn on", "turn off"])
    objects = [bed, fan]

    return Room(id, name, description, items, objects)

title()
player = buildPlayer()
room = buildBedroom()

# Print room information
print room.name
print room.description
room.print_room_items()
room.print_room_objects()
print

# Bed object action example
print room.objects[0].description
print "> make bed"
print "You make your bed. You notice your driver's license falls to the floor."
room.objects[0].status = False # Set messyBed to False
room.objects[0].description = "Your bed is made."

print "> look bed"
print room.objects[0].description

license = Item(3, "License", "Your driver's license.", None, None, False, True)
room.items.append(license)
room.print_room_items()



# Boolean values currently not created when room is created
# Add actions param to Room object as a list? Actions contain boolean vals for objects


