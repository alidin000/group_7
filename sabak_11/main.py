class Languages:
    def __init__(self,language,countries):
        self.language = language
        self.countries = countries
        print("Конструктор иштеди")
    def __str__(self):
        return f"bul til - {self.language} tili"
    
    def country(self):
        return self.countries


kyrgyz_tili = Languages("kyrgyz",['Kyrgyzstan'])
print(kyrgyz_tili)
print(kyrgyz_tili.language)

# kyrgyz tilin - озунчо класс кылып жарыяла
# Мурастоо - inheritance
# base/parent  - негизги/ата-эте класс 
# child / derived - бала класс
class Kyrgyz_tili(Languages):
    def __init__(self, language, countries):
        print("Bul kyrgyz tili classynyn contructoru")
        super().__init__(language,countries)
        # self.language = language
        # self.countries = countries

# class Kyrgyz_tili:
#     def __init__(self,language,countries):
#         self.language = language
#         self.countries = countries
#         print("Конструктор иштеди")
#     def __str__(self):
#         return f"bul til - {self.language} tili"
    
#     def country(self):
#         return self.countries

k_til = Kyrgyz_tili("кыргыз тили",['kyrgyzstan'])

print(k_til)
print(k_til.country())

class Zhanybarlar:
    def __init__(self,turu, age, tamagy):
        self.turu = turu
        self.age = age
        self.tamagy = tamagy
    
    def paidasy(self):
        return "adamga dos"
    
    def __str__(self):
        return f"Bul zhanybar - {self.turu}, {self.age} жашта жана {self.tamagy} жейт"
    
class It(Zhanybarlar):
    def __init__(self, turu, age, tamagy, aty):
        print("It contructoru inshtedi")
        self.aty = aty
        super().__init__(turu,age,tamagy)
        
    def paidasy(self):
        return super().paidasy() + " korgoochu"
    
    def __str__(self):
        return super().__str__() + f" aty = {self.aty}"

bobik = It("it", 2, "эт", "bobik")
print(bobik)
akdosh = It("it", 3, "эт", "akdosh")
print(akdosh)

class At(Zhanybarlar):
    def __init__(self, turu, age, tamagy, aty):
        print("At contructoru inshtedi")
        self.aty = aty
        super().__init__(turu,age,tamagy)

    # override / кайра аныктоо
    def paidasy(self):
        return super().paidasy() + ", adamdyn kanaty"
    
    def __str__(self):
        return super().__str__() + f" aty = {self.aty}"
    

akkula = At("жылкы",5,"чоп","Akkula")
print(akkula)
print(akkula.paidasy())

# Polymorphism => Poly = коп формалуу
zhanybarlar = [bobik, akkula, akdosh]

for zhanybar in zhanybarlar:
    print(type(zhanybar))
    print(zhanybar.paidasy())


# Encapsulation / private / public/ protected 
class Account:
    passwordd = "dfsdfads"
    __passwordd = "sdfasdf"
    _passwordd = "Bul protected attribute"
    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.password = password
        # self.__password = password

    def login(self, name, email, password):
        if self.name == name and self.email == email and self.password == password:
            return "Success"
        else:
            return "Failure"
k = Account("Ali","123345","ali@gmail.com")


# print(f"k.password = {k.__password}")
print(k.login("Ali","ali@gmail.com","12334"))
print(k.name)

class MurasClass(Account):
    def __init__(self, name, password, email, balance):
        self.__balance = balance
        super().__init__(name,password, email)

    def login(self):
        print(super()._passwordd)


p = MurasClass("sd", "34", "we@gmail.com", 34)
print(p.login())
print(p._passwordd)


class KopBurchtuktar:
    def __init__(self,burchtun_sany):
        self.burchtun_sany = burchtun_sany
    
    def __str__(self):
        return f"{self.burchtun_sany} burchtuk"
    
    def perimeter(self):
        return self.burchtun_sany * 4
    
    def area(self):
        return self.burchtun_sany ** 2

class UchBurchtuk(KopBurchtuktar):
    def __init__(self, burchtun_sany:int, biyiktik: int, jaktary: list[int]):

        if burchtun_sany != len(jaktary):
            raise Exception("Bul uch burchtuk emes!!!")

        self.biyiktik = biyiktik
        self.jaktary = jaktary
        super().__init__(burchtun_sany)
    
    def perimeter(self):
        return sum(self.jaktary)
    
    def area(self):
        return self.jaktary[0] * self.biyiktik / 2

t = UchBurchtuk(3, 2, [1,2,3])
print(f" perimeter = {t.perimeter()}")
print(f"area = {t.area()}")

p = UchBurchtuk(3,5,[3,4,6,4])