class Character:

    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []

    def __str__(self):
        s = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s

    def grab(self, item):
        self.inventory.append(item)

    def get_health(self):
        return self.health

def example():
        bob = Character("Bob", 20)
        print str(bob)
        bob.grab("pencil")
        bob.grab("papter")
        print str(bob)
        print "Health", bob.get_health()

example()
