st = "This class is about regular expression This"
soz = 'This'

# st textin ichinde jolugat
# barby?
i = 0
while i < len(st):
    j = 0
    temp = i
    while j < len(soz):
        if st[i] == soz[j]:
            j += 1
            i += 1
        else:
            break
    if j == len(soz):
        print(f"tabyldy")
        print(temp,i)
        print(st[temp:i]) 
    i = temp
    i += 1

import re # regular expression

# re.match() # окшошубу?
match = re.match(soz+"'s",st )
print(match)

# re.search() # издоо
print(re.search(soz, st))

print(f"result {re.findall(soz, st)}")

# * 
text = "ab*" "abb" "abbb" "ab" #  ( 0 же бир канча)
print("_______________")
print(re.match(r"s*", "sss Math ss")) #ssssss s ss sss
# .
# a. точканын ордуна 1 символ любой символ 

print("_______________")
print(re.findall(r"A..i","Alii Abi Adi A>i A3i"))

# ?
# a? => озуно чейинки элементти бир жолу койсо болот же болбойт
print("_)_)_)_)")
print(re.findall(r"aa?l","aaa4l aal al, ap a3 a-"))

print(re.findall(r"Ali?din", "Alidin, Aldin"))


# ^
# caret Тексттин башыны тандаш учун колдонулат 
# ^Dear
print(re.findall(r'^Dear', "Dear someone.,...."))

# + бул "*" окшош, жок дегенде 1 жолу болуш керек
# Hello Hellooooo 
# Hello+ 
print(re.findall(r'Hello+',"Helloo Hello Hell"))

#$ 
# тексттин аягын тандайт 
# .$
# ?$ 
print(re.findall(r'end$', "adf kajdfa df end"))
print(re.search(r'\.$', "adf kajdfa df end."))

# {}
# 12 1222 \d{2}
print(re.findall(r"\d{4}","asdf 2345 45 ads f12"))
print(re.findall(r"\d","asdf 2345 45 ads f12"))

# []
print(re.findall(r"[-+?.,]","asdf 2345 45 ads f12 ? , . - +"))

# |
# же ит|мышык
print(re.findall(r"cat|dog","this street is full of cats and dogs"))

sst = "A quantifier specifies how many instances of the previous element (which can be a character, a group, or a character class) must be present in the input string for a match to occur. Quantifiers include the language elements listed in the following table. For more information, see"

m = re.findall(r"or|group|element", sst)
print(m)


ttt = "123 432 234 23094 123 843 45 222"
print(re.findall(r"\d{3}",ttt))


text = "John's number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"
print(re.sub(pattern, "[REDACTED]", text))

text = "My name is Alidin and my number is 123-456-7890"
pattern = r"My name is (\w+) and my number is (\d{3}-\d{3}-\d{4})"
match = re.search(pattern, text)
print(match.groups())
print(match.group(1))  # Alidin
print(match.group(2))  # 123-456-7890

text = "Email me at alidin@example.com"
pattern = r"(\w+)@(\w+\.\w+)"
print(re.sub(pattern, r"\1[at]\2", text))