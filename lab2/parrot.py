from animal import Animal

class Parrot(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def express(self):
        print(f'{self.get_name()}: "Hello!"')
        print(r"   \   ")
        print(r"   (o> ")
        print(r"\\_//) ")
        print(r" \_/_) ")
        print(r"  _|_  ")

    def get_age_in_human_years(self) -> int:
        return self.get_age() * 5