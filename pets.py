class Pet():
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        if self.energy < 0:
            self.energy += 25
            if self.energy > 100:
                self.energy = 100
            return self
        else:
            print(f"{self.name} is not tired!")
            return self
    def eat(self):
        if self.energy < 100 and self.health < 100:
            if self.energy < 100:
                self.energy += 5
                if self.energy > 100:
                    self.energy = 100
            if self.health < 100:
                self.health += 10
                if self.health > 100:
                    self.health = 100
            return self
        else:
            print(f"{self.name} is not hungry.")
            return self
    def play(self):
        self.health += 5
        if self.health > 100:
            self.health = 100
        print(f"{self.name} is happy!")
        return self
    def noise(self):
        print(f"{self.name} makes whatever sounds a {self.type} makes...")
        return self

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def play(self):
        if self.health < 100:
            self.health += 5
            if self.health > 100:
                self.health = 100
            print(f"{self.name} plays happily!")
            return self
        else:
            print(f"{self.name} plays happily even though their health is 100%!")
            return self
    def noise(self):
        print(f"{self.name} woofs in approval!")

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def play(self):
        if self.health < 100:
            self.health += 5
            if self.health > 100:
                self.health = 100
            print(f"{self.name} humors you and plays along...")
        else:
            print(f"{self.name} can't be bothered at the moment...")
        return self
    def noise(self):
        print(f"{self.name} meows lazily...")
        return self
