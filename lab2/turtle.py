from animal import Animal

class Turtle(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def express(self):
        print(r"  _____     ____")
        print(r" /      \  |  o |")
        print(r"|        |/ ___\|")
        print(r"|_________/      ")
        print(r"|_|_| |_|_|      ")

    def get_age_in_human_years(self) -> int:
        return int(self.get_age() * 5.25)