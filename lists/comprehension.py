# lst = [1,23,4,5,6,7,6]
# sq_lst = [i**2 for i in lst]
# # print(lst)
# # print(sq_lst)

# even = [i for i in lst if i%2==0]
# odd = [i for i in lst if i%2!=0]
# # print(odd)
# # print(even)

# res = [i*i if i%2==0 else i+i for i in lst ]
# print(res)

# s = "india is my country"
# vow = ['a','e','i','o','u','A','E','I','O','U']
# temp = []
# # for i in s:
# #     if i in vow:
# #         temp.append(i)

# temp2 = [temp.append(i)  for i in s if i in vow]
# print(temp)

# lst1 = [2,3,4]
# lst2 = [2,4,6,8,9]
# res = []
# # for i in lst1:
# #     for j in lst2:
# #         if i!=j:
# #             res.append((i,j))
            
# print(res)

# lst3 = [res.append((i,j)) for i in lst1 for j in lst2 if i!=j ]
# print(res)

# res2=[]
# lst2=[res2.append((i**3)) for i in range(10)]
# print(res2)

lst = [1,2,3,4,5,6]
lst3 = [7,8,9,12,70,80]
print(list(zip(lst,lst3)))