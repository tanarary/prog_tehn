from person import Person
from parrot import Parrot
from turtle import Turtle

if __name__ == "__main__":
    parrot = Parrot("Kesha", 3)
    jack = Person("Jack", parrot)

    john = Person("John")
    jack.get_pet_info()
    john.get_pet_info()

    turtle = Turtle("Zavala", 4)
    john.set_pet(turtle)

    john.get_pet_info()