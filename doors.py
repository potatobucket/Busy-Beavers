class Door:
    def __init__(self, name):
        self.doorNumber = name
        self.closed = True
    
    def toggle_door(self):
        self.closed = not self.closed

def iterate_doors():
    numberOfDoors = 101
    doorList = [Door(i) for i in range(1, numberOfDoors)]
    for number in range(1, numberOfDoors):
        for door in doorList:
            if door.doorNumber % number:
                door.toggle_door()
    for index, portal in enumerate(doorList):
        print(f"Door {str(index + 1).zfill(3)} is {"closed" if portal.closed else "open"}")

if __name__ == "__main__":
    iterate_doors()
