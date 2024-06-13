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

#v.WAP to search for 13 in L
L= [14, 13, 12, 11] 
print(L.index(13))

#vi.WAP to count the number of elements present in L
print(len(L))

#vii.WAP to sum all the elements in L
sum = sum(L)
print(sum)

#viii.WAP to sum all ODD numbers in L
sum_odd = 0

for i in L:
    if i%2 != 0:
        sum_odd+=i

print(sum_odd)

#ix.WAP to sum all EVEN numbers in L
sum_even = 0

for i in L:
    if i%2 == 0:
        sum_even+=i

print(sum_even)

#x.WAP to sum all PRIME numbers in L
sum_prime = 0

for i in L:
    if i != 0:
        sum_odd+=i

print(sum_odd)