import sys, getopt
from animal import Animal
from dog import Dog
from cat import Cat
import math


#NOTE USE PYTHON 3 e.g. python3 main.py

#ALSO use a virtualenv as need pytest fo unit test example
#1.  python3 -m venv env
#2. source env\bin\activate.bat
#3. pip install pytest
#ß4. python rne_tipo_check.py

def main(argv):
    
    a = Animal.class_level_method()
    #you modify class method by referencing the class
    Animal.class_attribute_ex = "poo"
    print(Animal.class_attribute_ex) #will print poo
    
    #example of referencing an instance attribute  
    a.set_instance_attributes() 
    print(a.instance_attribute_ex)
    print(Animal.class_attribute_ex) #will print poo

    #example static method
    Animal.static_method_ex()
    a.static_method_ex()

    c,d = a.static_method__two_values_ex()
    print("c = {0}, d = {1}".format(c, d))

    print(a)

    #example of class level method
    #a.class_level_method()
    a.class_level_method()

    #example of using constructor
    b = Animal.class_level_method()
    print(b.instance_attribute_ex)

    #public, private, protected variables example
    print(b.instance_attribute_ex) #public
    #print(b.instance_private_ex) #private. Python enforces this access. But it is name mangled and can still be accessed via the mangled name - but should not
    print(b._instance_protected_ex) #protected. Python does not enforce protected, this is convention


    #inheritance exmaples
    d = Dog() 
    print(d.class_attribute)

    #polymorphism example
    c = Cat()
    print_what_am_i(c)

    #call a property of animal
    print(a.me)

    #call its setter
    a.me = "blah"
    print(a.me)

    #lisy slicing examples
    a = ('X','Y','Z','A','B','C')
    
    #list is 0 offset
    start = 1
    stop = 3
    print(a[start:stop])  # items start through stop-1
    print(a[start:]  )    # items start through the rest of the array
    print(a[:stop])       # items from the beginning through stop-1
    print(a[:] )          # a copy of the whole array
    print(a[len(a)::-1] )          # reverse a

  

    
        




def print_what_am_i(a):
    a.what_am_i()


if __name__ == "__main__":
   main(sys.argv[1:])