# 3] Acessing item from LIST

# A] acessing 1D array is very similar to STR

l1 = [1, 2, 3, "Ramos", 6.0]
print(l1)

print(l1[0], l1[-1], )
print(l1[0:5])
print(l1[::-1])

# B]Multi Dimensional Array is Bit Diffrent


l2d = [1, 2, 3, [4, "This"], 7, 8, 99]
print(l2d[3][1])


l2d = [1, 2, 3, [4, 5, [88, "3D-List"]]]
print(l2d[3][2][1])

""" NOTE
 no of brackets used to acess list= dimension of List
i.e: 2 bracs for 2D list 
     n bracs for nD list
"""
