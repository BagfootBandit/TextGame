from World import overworld, cave, locations

#locations[map[y][x]] -> Location?

class map():
    def __init__(self, map):
        self.map = map
        self.events = {
                0: self.boring,
                1: self.boring,
                2: self.boring,
                3: self.boring,
                4: self.attacked,
                5: self.boring,
                6: self.roll,
                7: self.boring,
                }

    def event(self, x, y):
        location = self.map[y][x]
        self.events[location](location)

    def boring(self, location):
        pass

    def attacked(self, location):
        if location == 4:
            print("There is a troll guarding his cave!")
            input("Attack?")
        pass

    def roll(self, location):
        pass

class player():
    def __init__(self, name):
        self.x = 1
        self.y = 1
        self.name = name
        self.map = map(overworld)

    def go(self, direction):
        if direction == "south" and self.y < (len(self.map.map) - 1):
            self.y += 1
        elif direction == "north" and self.y > 0:
            self.y -= 1
        elif direction == "east" and self.x < (len(self.map.map[0]) - 1):
            self.x += 1
        elif direction == "west" and self.x > 0:
                self.x -= 1
        else:
            print("I can't go there.")

    def enter(self):
        loc = self.map.map[self.y][self.x]
        if loc == 4:
            self.map = map(cave)
            self.x = 2
            self.y = 2
        elif loc == 5:
            self.map = map(overworld)
            self.x = 3
            self.y = 3
        else:
            print("I can't enter here...")

    def location(self):
        return locations[self.map.map[self.y][self.x]]

if __name__ == "__main__":
    print("\nWelcome to TextGame!")
    player1 = player(input("What's yer name bucky?"))
    print("You are in " + player1.location())
    action = [""]
    while action[0] != "Exit":
        inbound = input("Action: ")
        action = inbound.split()
        if action[0] == "go":
            try:
                player1.go(action[1])
            except:
                print("I can't go there.")
            print("You are in " + player1.location())
        elif action[0] == "enter":
            try:
                player1.enter()
            except:
                print("I can't enter here.")
            print("You are in " + player1.location())

    print("You are in " + player1.location())
    print("\nGoodBye, " + str(player1.name) + "!")
