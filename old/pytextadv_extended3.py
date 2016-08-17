def title():
    print "+---------------------------------------+"
    print "| Text Adventure Skeleton Code (Python) |"
    print "+---------------------------------------+"
    print "v1.0"
    print "Programmed by Daniel Hagquist, 7/1/2016."
    print "View readme.txt for more information."
    print

class Player:
    def __init__(self, name, status, inventory, health, score, weapon):
        self.name = name
        self.status = status
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
    def __init__(self, id, name, description, status, actions, weapon, food, canpickup):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.actions = actions
        self.weapon = weapon
        self.food = food
        self.canpickup = canpickup

class Object:
    def __init__(self, id, name, description, status, actions):
        self.id = id
        self.name = name
        self.description = description
        self.actions = actions

class Weapon:
    def __init__(self, id, name, description, power, quality):
        self.id = id
        self.name = name
        self.description = description
        self.power = power
        self.quality = quality

def buildPlayer():
    name = raw_input("Please enter your name: ")
    status = "You are ready to embark on your adventure."
    inventory = []
    health = 100
    score = 0
    weapon = "None"
    player = Player(name, status, inventory, health, score, weapon)
    print "Hello, " + player.name + ".\n"
    return player

def buildWorld():
    mapwidth = 2
    mapheight = 2
    world = [[0 for x in range(mapwidth)] for y in range(mapheight)]
    
    def buildBedroom():
        id = 1
        name = "Bedroom"
        description = "This is your childhood bedroom."
        # Items (able to added to inventory)
        walletHasLicense = False
        wallet = Item(1, "Wallet", "Your wallet is made of the finest of faux leather.",
                      walletHasLicense, ["open", "close"],
                      False, False, True)
        keyUsed = False
        key = Item(2, "Key", "A single key with which you are unfamiliar.",
                      keyUsed, ["use", "unlock"],
                      False, False, True)
        items = [wallet, key]
        # Objects (unable to be added to inventory)
        messyBed = True
        bed = Object(1, "bed", "Your bed is very messy.", messyBed, ["make bed"])
        fanOff = True
        fan = Object(2, "ceiling fan", "The fan hasn't been cleaned in years.", fanOff,
                     ["turn on", "turn off"])
        objects = [bed, fan]
        exists = True
        exits = ["n", "s"]
        return Room(id, name, description, items, objects, exists, exits)

    def buildBathroom():
        id = 2
        name = "Bathroom"
        description = "The bathroom is moldy and damp."
        # Items (able to added to inventory)
        magazineOpen = False
        magazine = Item(3, "Magazine", "Reading material.", magazineOpen,
                        ["open", "close", "read"], False, False, True)
        tweezers = Item(4, "Tweezers", "You never know when you might need them.", None,
                        ["use", "pick"], False, False, True)
        items = [magazine, tweezers]
        # Objects (unable to be added to inventory)
        toiletUsed = False
        toilet = Object(3, "toilet", "Yeap. That's a toilet.", toiletUsed, ["use"])
        showerOn = False
        shower = Object(4, "shower", "You rarely spend time in here.", showerOn,
                        ["turn on", "turn off"])
        objects = [toilet, shower]
        exists = True
        exits = ["n", "s"]
        return Room(id, name, description, items, objects, exists, exits)

    def buildKitchen():
        id = 3
        name = "Kitchen"
        description = "This is the kitchen."
        # Items (able to added to inventory)
        appleEaten = False
        apple = Item(5, "Apple", "It looks delicious.", appleEaten, ["eat"],
                     False, True, True)
        chainsawOn = False
        chainsaw = Item(6, "Chainsaw", "Who leaves a chainsaw in the kitchen?",
                      chainsawOn, ["use"], False, False, True)
        items = [apple, chainsaw]
        # Objects (unable to be added to inventory)
        clock = Object(5, "clock", "The clock reads 3:33.", None, ["read"])
        fridgeOpen = False
        fridge = Object(6, "fridge", "The fridge was made in the 1950s.", fridgeOpen,
                        ["open", "close"])
        objects = [clock, fridge]
        exists = True
        exits = ["n", "s"]
        return Room(id, name, description, items, objects, exists, exits)

    def buildGarage():
        id = 4
        name = "Garage"
        description = "The garage smells like gasoline."
        # Items (able to added to inventory)
        gasolineFull = True
        gasoline = Item(7, "Gasoline", "It stinks!", gasolineFull,
                        ["use", "put", "fill"], False, False, True)
        screwdriver = Item(8, "Screwdriver", "This could come in handy.",
                      None, ["use"], False, False, True)
        items = [gasoline, screwdriver]
        # Objects (unable to be added to inventory)
        carLocked = True
        car = Object(7, "car", "It's a 1982 Honda Civic hatchback.", carLocked,
                     ["unlock", "get in", "start", "turn off"])
        garageDoorClosed = True
        garagedoor = Object(8, "garage door", "The garage door can open and close.",
                            garageDoorClosed, ["open", "close"])
        objects = [car, garagedoor]
        exists = True
        exits = ["n", "s"]
        return Room(id, name, description, items, objects, exists, exits)


    world[0][0] = buildBedroom()
    world[0][1] = buildBathroom()
    world[1][0] = buildKitchen()
    world[1][1] = buildGarage()
    return world

title()
player = buildPlayer()
world = buildWorld()

# Test
world[1][1].print_room_items()
world[1][1].print_room_objects()

# Test opening garage door and closing
print world[1][1].id
print world[1][1].name
print world[1][1].description

# Boolean values currently not created when room is created
# Add actions param to Room object as a list? Actions contain boolean vals for objects


