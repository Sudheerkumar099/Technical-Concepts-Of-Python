import copy
lst1 = [1,2,3,5,5]
# print(len(lst1))
# print(max(lst1))
# print(min(lst1))
# print(sum(lst1))

# for i,j in enumerate(lst1):
#     print(i,j)  #give values along with the index
lst2 =   copy.deepcopy(lst1)  

lst1.append(50)
lst1.remove(50)
lst1.extend(lst2)    
print(lst1)

print(lst1.count(5))
print(lst1.index(2))
print(lst1.pop(5))
# print(lst1.reverse())
print(lst1.index(2,4,6))
# lst1.clear()
# sorted(lst1) #used for sorting the list
print(lst1)
sorted(lst1) #used for ascending order sorting
lst1.sort(reverse=False) #used for ascending
print(lst1)
lst1.sort(reverse=True)# used for decending
print(lst1)

print(list(reversed(lst2)))# used for the reversing
lst1.reverse()
print(lst1)


        

