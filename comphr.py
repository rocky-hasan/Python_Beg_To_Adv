# or_list=[1,2,3,4,5]
# # copy_list=[elements for elements in or_list]
# copy_list=or_list.copy()
# print(copy_list)

# x1='hello world'.split()
# x2='hello pink'.split()
# y1=set(x1)
# y2=set(x2)
# res=y1.symmetric_difference(y2) # when we use set then symmetric works
# print(res)

# x='hello world'
# d={}
# for i in x:
#     if i in d:
#         d[i] +=1
#     else:
#         d[i]=1
# dup=[]
# # for k,v in d.items():
# #     if d[k]>1:
# #         dup.append(k)

# newlist=[k for k,v in d.items() if d[k]>1]
# print(newlist)
# # print(d)
# # print(dup)
# dict1 = {'a': 1, 'b': 2}
# dict2={'c':8}
# merg={**dict1,**dict2}
# print(set(merg))
# key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
# flat={}
# for k,v in key_values_list:
#     flat[k]=v
# print(flat)
#--------------Comphrehension-----------::::::::::::::::::::::::
# X, Y = map(int, input("Enter two digits (X, Y): ").split(','))
# print(X,'=',Y)
# matrix = [[i*j for j in range(Y)] for i in range(X)]
# # for i in range(X):
# #     for j in range(Y):
# #         matrix[i][j]=i*j

# for row in matrix:
#     print(row)        without,hello,bag,world
# string_seq=input("Enter string :")
# newstring=string_seq.split(',')
# newstring_sort=sorted(newstring)
# afterstring=','.join(newstring_sort)
# print(afterstring)
input_sequence="enter a new word and do and"
word=set(input_sequence.split())
newword=sorted(word)
lastword=' '.join(newword)
print(*newword)