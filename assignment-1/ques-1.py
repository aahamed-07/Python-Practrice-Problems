#Question 1 

#i.WAP to add 50 and 60 to L
L= [11, 12, 13, 14]

L1 = [50,60]

L2 = L + L1
print("New List after adding 50,60: ",L2)

#ii.WAP to remove 11 and 13from L
L= [11, 12, 13, 14]
del L[0]                #indices have shifted after first deletion
del L[1]
print("List after removing 11,13: ",L)

#iii.WAP to sort L in ascending order
L= [13, 12, 14, 11]         #Random List  
L.sort()
print("Sorted List: ",L)

#iv.WAP to sort L in descending order
L= [13, 12, 14, 11]         #Random List  
L.sort(reverse=True)
print("Sorted List Descending order: ",L)