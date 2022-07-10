max_scoops = 3


class IceCream():
    def __init__(self):
        self.scoop = max_scoops

    def Eat(self, scoop):
        if self.scoop <= 0:
            print(f"No scoop left, TopUp!")
        elif scoop > self.scoop:
                print(f"You have {self.scoop} to eat")
        else:
            self.scoop -= scoop
            print(f"Scoop remaining {self.scoop}")

    def TopUp(self, scoop):
        self.scoop += scoop
        if self.scoop > max_scoops:
            print(f"Too many Scoops, Cone dropped!")
            self.scoop = 0
        else:
            print(f"Cone topped with {scoop}, enjoy {self.scoop} scoops")