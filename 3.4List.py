# 5] Delete
""" 
    A]del--> DELETE ENTIRE list or SPECIFIC elemrnt
    B]remove -->used to remove SPECIFIC item by mentioning the ITEM NAME
    C]pop--> POPS/DELETES LAST item
    D]clear-->makes list EMPTY

"""

# A] del

l = [1, 2, 3, 4]
# del l deletes entire list

del l[2]
print(l)


# B] remove

l1 = ["my", 3, 4, 5, 6, "name", True]
l1.remove('name')
print(l1)

# C] pop

l1.pop()
print(l1)


# D] clear
l1.clear()
print(l1)
