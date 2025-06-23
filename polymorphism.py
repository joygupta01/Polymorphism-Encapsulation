class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a Dog. My name is {self.name}. I am {self.age} years old")

    def sound(self):
        print("Bark")  

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a Cat. My name is {self.name}. I am {self.age} years old")

    def sound(self):
        print("Meow")  

cat1 = Cat("Hia",4)
dog1 = Dog("Dixcy",8)

for animal in (cat1,dog1):
    animal.info()
    animal.sound()