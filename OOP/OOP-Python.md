# Python OOP

## 1. What Is OOP?

OOP (Object-Oriented Programming) is a programming style where we
structure our code using classes and objects.

### OOP helps you:

-   Organize code
-   Reuse code (inheritance)
-   Protect data (encapsulation)
-   Build real-world models (objects)

------------------------------------------------------------------------

## 2. Class and Object

**Class** → A blueprint/template for creating objects.\
**Object** → An instance of a class.

``` python
class Person:
    pass

person1 = Person()
```

------------------------------------------------------------------------

## 3. Attributes and Methods

-   **Attributes** → Variables inside a class\
-   **Methods** → Functions inside a class

``` python
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}"

p1 = Person("Ebraam", 22)
print(p1.greet())
```

------------------------------------------------------------------------

## 4. The `__init__` Constructor

Runs automatically when creating an object.

``` python
def __init__(self, name):
    self.name = name
```

------------------------------------------------------------------------

## 5. `self` Keyword

`self` refers to the current object.

------------------------------------------------------------------------

## 6. Encapsulation (Data Protection)

``` python
class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance
```

------------------------------------------------------------------------

## 7. Inheritance

``` python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # inherits from Animal
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())
```

------------------------------------------------------------------------

## 8. Multiple Inheritance

``` python
class A:
    def method_a(self):
        return "A"

class B:
    def method_b(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.method_a(), c.method_b())
```

------------------------------------------------------------------------

## 9. Polymorphism

``` python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"
```

------------------------------------------------------------------------

## 10. Abstraction

``` python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

------------------------------------------------------------------------

## 11. Class Methods & Static Methods

### Class Method

``` python
class Student:
    school = "ABC School"

    @classmethod
    def get_school(cls):
        return cls.school
```

### Static Method

``` python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

------------------------------------------------------------------------

## 12. Magic (Dunder) Methods

  `__init__`      Constructor

  `__str__`       String representation

  `__len__`       Length behavior

  `__add__`       Behavior for + operator

  `__getitem__`   Indexing behavior

---

``` python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages
```

------------------------------------------------------------------------

## 13. OOP Examples

``` python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} - {self.year}"

class ElectricCar(Car):
    def __init__(self, brand, year, battery):
        super().__init__(brand, year)
        self.battery = battery

    def info(self):
        return f"{self.brand} - {self.year} - {self.battery} kWh"
```
---
```python
class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)
```