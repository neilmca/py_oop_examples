
def animal_func():
    return "blah"

class Animal(object):


    #this overides the standard str method
    def __str__(self):
        return "Animal class Object"

    #this is a construtor
    def __init__(self, sub_type):
        print("in Animal.__init__")
        self.instance_attribute_ex = 0 #this is a public variable
        self.__instance_private_ex = 1 #this is a private variable
        self._instance_protected_ex = 2 #this is a protected variable

        self.__sub_type = sub_type


    #this is a class attribute that is shared by all objects of a class
    #these are basically static variables
    class_attribute_ex = "animal"

    #this is a class level method. 
    # Note it has a reference to cls so you can use it to create an instance
    @classmethod
    def class_level_method(cls):
        print("I am a class level method. Useful to be used a factory to create an instance")
        return cls("animal")


    #this is a instance method that is setting an instance attribute
    #It is an instance method as first arg is self
    #instance attributes are basically member variables
    #since python can dynamically bind variables you don't have to set in class definition like 
    #you would for C#
    def set_instance_attributes(self):
        self.instance_attribute_ex = 4
        Animal.class_attribute_ex = "wee" #you can change class attributes


    @staticmethod
    def static_method_ex():
        print ("static methods can be called via Class or instance")

    @staticmethod
    def static_method__two_values_ex():
        print ("sfrom methods you can return multiple values")
        return 3,5

    def what_am_i(self):
        print("don't know - some animal")


    #property decorator makes a getter available that looks like an attribute
    #so can call it a.me 
    @property
    def me(self):
        return self.__sub_type

    #this makes a setter for the me property
    @me.setter
    def me(self, sub_type):
        self.__sub_type = sub_type

    

    