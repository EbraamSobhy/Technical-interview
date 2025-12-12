class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep!"

def make_sound(obj):
    print(obj.speak())  # No matter what the object is!

make_sound(Dog())
make_sound(Cat())
make_sound(Robot())