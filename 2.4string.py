# String specific functions


# 1. Capitalize/Title/Uppercase/Lowercase/Swapcase
c = "MY name is KhaNnn"

print(c.capitalize())  # capitalizes first letter of string

print(c.title())  # caps all word first letter of string

print(c.upper())  # anycase to upper case

print(c.lower())  # to lowercase


# 2. Count
print(c.count("Nnn"))  # returns the no of time a substr or alp is repeated in str
print(c.count("a"))
print(c.count("sonar"))


# 3.Find/Index
c = "this is the realm"

# Find
print(c.find("m"))  # returns index of alp or sstr
print(c.find("realm"))
print(c.find("n"))  # if not found it returns -1

# Index
# print(c.index("n")) #same as find but it throws error instead of -1


# 4. endswith/startswith

print(c.startswith("th"))

print(c.endswith("ook"))


# 5.format

c = "My name is{}, my age is{}"

print(c.format("Anthony", 67))

print("Hello Mr.{u_name}, Call me {b_name}".format(
    u_name="Ram", b_name="45yus"))

print("Hi{1}, I am {0}".format("ram", 89))


# 6. isalnum/isalpha/isdecimal/isdigit/isidentifier
print("sd")
# used to check whether string is alpha-numeric or...
print("skib45".isalnum())
print("_name".isidentifier())
print("90name".isidentifier())


# 7. split
# used to split str; used to generate tags
c = "This is a sci-fi movie rated 'R'"

print(c.split())
print(c.split("sci-fi"))


# 8. join
# sort of opposite of split
k = " me ".join(['this', 'is', 'lamda'])
print(k)


# 9. Replace
# swaps string component with new component
p = "Hi I am ramos".replace("ramos", "vamos")
print(p)


# 10.strip
# removes whitespace at beginning and end but not of middle!; useful in webdev
c = "   argen tina    "
print(c)
print(c.strip())
