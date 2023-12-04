"""
    -->Strings are immutable Data type
    -->Basic Data Types(int, float, complex, boolean, STRING)
    -->STRING:
"""


# 1. Creating String
print("This is a String")
print('Python doesnot have "character"')

# 2.Acessing Substring from strings

# A] Indexing
c = "hellkooi"
print(c[0])  # +ve indexing
print(c[5])

print(c[-1])  # -ve indexing
print(c[-4])

# B] Slicing
v = "This is an interger"
print(v[0:4:1])  # positive indexing
print(v[0:7:3])    # v[start:end-1:increment]

print(v[5:0:-1])  # negative slicing
# reverse a string:
print(v[::-1])
