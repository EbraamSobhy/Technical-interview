# Objects
### An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

## An object consists of:

### - State: It is represented by the attributes and reflects the properties of an object.

### - Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.

### - Identity: It gives a unique name to an object and enables one object to interact with other objects

```py
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name) 
print(dog1.species)
```
---
## Self Parameter
### Self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.

```py
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 5)  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly
```
---

## __init__ Method
### __init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.

```py
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
print(dog1.name)
```
### __init__: Special method used for initialization.
### self.name and self.age: Instance attributes initialized in the constructor.




