import re

# re.match
# re.search
# re.findall()

# .
# +
# ?
# $
# ^
# *

# metacharacters 
# /d -> digit цифра
print(re.findall(r'\d', "d 3 12"))
print(re.findall(r'\d+', "d 3 12")) #  1 je andan jop
print(re.findall(r'\d*', "d 3 12")) # 0 je andan kop
print(re.findall(r'\d?', "d 3 12")) 
print(re.findall(r'\d$', "d 3 12")) 
print(re.findall(r'^\d', "6d 3 12")) 
print(re.findall(r'\d{2}', "6d 3 12")) 
print("HERE: ",re.findall(r'\d{0}[1234]', "6d 3 1234")) 



# /D -> anti inverse (/d ) цифра эмес 
print(re.findall(r'\D', "d 3 12"))

# /w -> character ([a-zA-Z0-9_])
print(re.findall(r'\w', "d 3 12"))
print("HERE + ",re.match(r'(\w+) (\w+) (\w+)', "d 3 12").groups())

# /W -> character ([a-zA-Z0-9_]) ушудан башка баары кирет
print(re.findall(r'\W', "d 3 12?"))

# /s space -> boshtuk
print(re.findall(r'\s', "d 3 12"))

# /S inverse boshtuk, boshtuk
print(re.findall(r'\S', "d 3 12"))

# () 
# pattern => r'/w+ (/d{1}) /w+'
print("_)_)_)_)_)_)_)()_()")
match = re.match(r'(.+) (.) (.+) \?', "fasdfd 3 kljjk ?")
print(match)
print(match.group(0))
print(match.group(1))
print(match.groups())

# re.sub() -> substitue => ордуна коюу
text = "Today's class is 17th"
pattern = r'\d{2}'
repl = "18"
print(re.search(pattern, text))
output = re.sub(pattern=pattern, repl=repl, string=text)
print(f"substituted text:{output}")

text2 = "THe number is 123-234"
repl = "[DOESN'T EXIST]"

print(re.sub(pattern=r'\d{3}-\d{3}', repl=repl, string=text2))


text3 = "My name is - Alidin !!!"
pattern = r'(\w+) (\w+) (\w+) - (.+!!!)'
print(re.search(pattern, text3))
print(re.sub(pattern,r'\1 \2 \3 сызыкча \4', text3))


phone_numbers = "My new phone number is +996-779-996-954"

pattern = r"\+\d{3}-\d{3}-\d{3}-\d{3}"
pattern = r"\+996-\d{3}-\d{3}-\d{3}"

print(re.findall(pattern, phone_numbers))
print(re.sub(pattern, "[Not found]", phone_numbers))

email = "new email = newemail@inbox.com"
pattern = r'\w+@\w+\.\w{3}'

print(re.findall(pattern, email))


print(re.match(r'(.+)@.+', "john.doe@gmail.com").groups())