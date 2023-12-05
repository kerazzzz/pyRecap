# 4] Editing List

# unlike str list are mutable

# A
L = ['ok', 1, 3]
L[0] = 'nook'
print(L)

L[0:] = [1, 2, 3]
print(L)


# B]Editing List

"""
    i)append   -->adds ONLY 1 item at END of list
    ii)extend  -->adds MULTIPLE  item at END of list
    iii)insert -->adds item at SPECIFIC position

"""
l = ["first", 2, 3, True, 6]

# i) append

l.append(5)
# l.append(5,9) this throws an error as append can only insert 1 item not more than that
print(l)

l.append([5, 6, 7])
print(l)

# ii)extend

# note: the items to be added should be in list format
l.extend([34, 444, 511, 666])
print(l)

# l.extend(999) this throws an error as extend is used to add multiple item not 1 item
l.extend(["apple", "banana"])
# l.extend("apple") TRY!! ;)
print(l)


# iii)insert

lz = ["cow", 3, 6, 7]
lz.insert(1, 1)
print(lz)
