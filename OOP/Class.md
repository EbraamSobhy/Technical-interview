# Class
### A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

## Some points on Python class:  

### - Classes are created by keyword class.
### - Attributes are the variables that belong to a class.
### - Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

```py
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
```


