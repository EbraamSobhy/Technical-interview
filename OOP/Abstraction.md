# Abstraction

### It is the process of hiding the internal details of how something works and showing only the necessary functionality to the user.

### Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on "what to do" rather than "how to do it."

### Think of it like driving a car:
### You use the steering wheel, accelerator, and brakes.
### You don’t need to know how the engine works internally.
### In Python, abstraction helps simplify complex systems by hiding implementation details.

<br>

![Alt text](Encapsulation.webp)

## Types of Abstraction:

### 1. Data protection: Prevents direct access to sensitive attributes.
### 2. Control over data: You can validate data before updating it.
### 3. Flexibility: Internal implementation can change without affecting external code.
---
## Types of Encapsulation:
### 1. Partial Abstraction: Abstract class contains both abstract and concrete methods.
### 2. Full Abstraction: Abstract class contains only abstract methods (like interfaces).

<br>

```py
class Dog:
    def __init__(self, name, breed, age):
        self.name = name # Public attribute
        self._breed = breed # Protected attribute
        self.__age = age # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid")

dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())
```
---
## Explanation:

### - Public Members: Easily accessible, such as name.
### - Protected Members: Used with a single _, such as _breed. Access is discouraged but allowed in subclasses.
### - Private Members: Used with __, such as __age. Access requires getter and setter methods.

