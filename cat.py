from animal import Animal


class Cat(Animal):

    class_attribute = "I am a cat"

    def __init__(self):
        super().__init__("dog")

    def what_am_i(self):
        print(Cat.class_attribute)