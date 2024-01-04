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
# input_sequence="enter a new word and do and"
# word=set(input_sequence.split())
# newword=sorted(word)
# lastword=' '.join(newword)
# print(*newword)

# def fibo(num):
#     sequence=[0,1]
#     [sequence.append(sequence[-1]+sequence[-2]) for _ in range(2,num)]
#     return sequence
# try:
#     n=int(input("Enter the number: "))
#     result=fibo(n)
#     print(result)
# except ValueError:
#     print("Invalid Number")

# def amply(number):
#     result=[num*10 if num%4==0 else num for num in range(1,number+1)]
#     return result
# print(amply(4))


# def unique(number):
#     dictionary={}
#     for num in number:
#         if num in dictionary:
#             dictionary[num] +=1
#         else:
#             dictionary[num]=1
#     for num,count in dictionary.items():
#         if count==1:
#             return num
# res=unique([3, 3, 3, 7, 3, 3])
# print(res)
# from collections import Counter
# def unique(number):
#     unique=[num for num,count in Counter(number).items() if count==1]
#     return unique
# numbers = unique([1,  1, 2, 3, 4,2,3])
# print(numbers)

# dict_to_list=({
#  "D": 1,
#  "B": 2,
#  "C": 3
# })
# list1=[(key,value) for key,value in dict_to_list.items()]
# print(list1)
# print(type(list1))

# def mapping(list1):
#     dec={}
#     for list2 in list1:
#         dec[list2]=list2.upper()
#     return dec
# res=mapping(["q", "s"]) 
# print(res)


# def repvowel(string, vowel):
#     vowels = "aeiou"
#     result = ''.join([vowel if char in vowels else char for char in string])
#     return result

# # Example usage:
# new_string = repvowel("hello world", "u")
# print(new_string)


