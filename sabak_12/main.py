# abstract classes => toluk emes class
# класстын структурасы же логикасы эле жазылып, бирок озунон объекттерди жасаса болбойт

class Temp:
    def __init__(self, something):
        self.sth = something

t = Temp("asdf")

from abc import ABC, abstractmethod

# abstract class
class AbstractClass(ABC):
    def __init__(self,something):
        self.sth = something
        print("Abstract class jasaldy")

    # abstract method
    @abstractmethod
    def print_2(self):
        pass

    #simple method
    def print(self):
        print("Hello world")

# tempt = AbstractClass("adf ")


class MuraskerClass(AbstractClass):
    
    def print_2(self):
        print("Implemented here!")

tempt_2 = MuraskerClass("adf ")


class Programmers(ABC):
    def __init__(self,name, field):
        self.name = name
        self.field = field
    
    def __str__(self):
        return f"Programmist: {self.name}, works in field: {self.field}"
    
    @abstractmethod
    def write_code(self):
        pass

# pt = Programmers("Omar", "frontend")

class Pythonist(Programmers):
    def write_code(self):
        print('print("Hello world")')

class Java(Programmers):
    def write_code(self):
        print('System.println("Hello world");')

class Cpp(Programmers):
    def write_code(self):
        print('cout << "Hello world << endl;"')


ptt = Pythonist("Omar", "data scientist")
qw = Java("Jumash", "backend")
we = Cpp("John", "game development")
ptt.write_code()
print(ptt, qw, we)


# interface => бардык методдору abstract 

class Interface(ABC):
    @abstractmethod
    def do_something(self):
        pass
    @abstractmethod
    def write_something(self):
        pass

    @abstractmethod
    def solve_something(self):
        pass

class InterfaceChild(Interface):
    def __init__(self,*args):
        self.args = args

    def do_something(self):
        i = 9
        while i >= 0:
            if i % 7 == 1:
                print(f"i = {i}")
            i -= 1 # i = i - 1 # i--

    def write_something(self):
        l = ["I", "like", "python"]
        w = ""
        for word in l:
            w = w +" "+ word
        print(w)

    def solve_something(self):
        t = [1,2,4,5,5,6,6,7]
        print(f"sorttogongo cheiin: {t}")
        for i in range(len(t)):
            for j in range(len(t)):
                if t[i] > t[j]:
                    t[i] , t[j] = t[j], t[i]
                    # t[i] menen t[j] maanisin almashtyryp atam
                    # temp = t[i]
                    # t[i] = t[j]
                    # t[j] = temp
        print(f"sorttogondon kiyin: {t}")

interface = InterfaceChild("bul men", 12)

interface.do_something()

print("____")
interface.write_something()
print("____")
interface.solve_something()

class Animals(ABC):
    
    @abstractmethod
    def eat_something(self):
        pass

class Pets(Animals):
    @abstractmethod
    def lives_outside(self):
        pass

class Cat(Pets):
    def lives_outside(self):
        return True
    
    @abstractmethod
    def type(self) -> int:
        pass

class OrangeCat(Cat): 
    def type(self, d) -> None:
        print(d)

    def eat_something(self):
        pass

l = OrangeCat()
l.type("print")

class Lion(Animals):
    
    def eat_something(self):
        print("Lion eats meat")

class Goat(Animals):
    def eat_something(self):
        print("Goat eats grass")

class Shark(Animals):

    def eat_something(self,argument):
        print("Sharks eats fishes")
        print(argument)

s = Shark()
s.eat_something("3")


class City:
    def __init__(self, population):
        self.pop = population

    def __add__(self, city):
        result = City(self.pop + city.pop)
        return result
    def __sub__(self, city):
        result = City(self.pop - city.pop)
        return result

    def __eq__(self, city):
        return self.pop == city.pop
    
    def  __str__(self): 
        return f"city with {self.pop} population"

city1 = City(12)
city2 = City(12)

print(city1 + city2)
print(city1 - city2)
print(city1 == city1)
