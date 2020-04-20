from animal import Animal


class Dog(Animal):

    class_attribute = "I am a dog"

    def __init__(self):
        super().__init__("dog")

    def what_am_i(self):
        print(Dog.class_attribute)