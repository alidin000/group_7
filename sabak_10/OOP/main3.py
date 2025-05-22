# OOP - Object oriented programming - Объектно оринтированное программирование
# procedure - процедурный

at = "ali"
jash = 13
salmagy = 23.4

def print_adam(**kwargs):
    print(kwargs)

print_adam(at = "ali", jash = 13,salmagy = 23.4)


# class озундо озгормолорду жана функцияларды камтый алат

class Adam:
    # конструктор
    def __init__(self,at, jash, salmagy):
        self.at_2 = at
        self.jash_2 = jash
        self.salmagy_2 = salmagy
    
    # функция, метод
    def print_adam(self,temp):
        print(self.at_2)
        print(self.jash_2)
        print(self.salmagy_2)
        print(temp)

adam1 = Adam("ali", 23, 45.5)
adam1.print_adam("tasdfadsfsd")
# print(adam1.salmagy_2)
# print(adam1.at_2)
# print(adam1.jash_2)

def print_adam(d):
    print(d)
    # print(self.at_2)
    # print(self.jash_2)
    # print(self.salmagy_2)

print_adam(3)

class Animals:
    place = "city"
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def  __str__(self):
        return f"at = {self.name} jash={self.age} tus={self.color}"
dog = Animals("Bobik", 5, "ak")
# __str__ function ga cheiun => <__main__.Animals object at 0x0000025255D17A70>
# __str__ jazgandan kiyin => at = Bobik jash=5 tus=ak
print(dog)
print(dog.place)

class Cars:
    type_1 = "BMW"
    color = "green"

car = Cars()
print(car)
print(car.color)
print(car.type_1)


class ProgrammingLanguages:
    language = "C++" # аттрибут
    
    def __init__(self,language,**kwargs):
        print("pustoi emes constructor")
        self.language = language
        if "year" in kwargs:
            self.year = kwargs['year']
        else:
            self.year = 2000

    # def __init__(self):
    #     print("Pustoi constructor")

    def  __str__(self):
        return f"this is {self.language}, year = {self.year}"

    def temp_2(self): # метод
        print("hello")
    

python = ProgrammingLanguages("python", year=1999)
java = ProgrammingLanguages("python")
Cpp = ProgrammingLanguages("python")

# languages = [python, java]
# print(languages)
print(python)
print(java)
print(Cpp)
print(Cpp.temp_2())
# print(Cpp.temp_function())
