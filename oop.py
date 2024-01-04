# class Shape:
#     def __init__(self) -> None:
#         pass
#     def area(self):
#         return 0
# class Square:
#     def __init__(self,length) -> None:
#         super().__init__()
#         self.length
#     def area(self):
#         return self.length**2
# shape = Shape()
# square = Square(float(input("Enter the shape of the square: ")))
# print("Shape's area by default:", shape.area())
# print("Area of the square:", square.area()) 


# def treearg(a,b,c):
#     total=0
#     for i in range(a,b+1):
#         if i%c==0:
#             total=total+i
#     return total
# result=treearg(1,10,2)
# print(result)


# def compare(str1,str2):
#     if len(str1)!=len(str2):
#         print("Not compareable")
#     else:
#         destance=0
#         for i in range(len(str1)):
#             if str1[i]!=str2[i]:
#                 destance +=1
#         return destance

# result=(compare('abcde','abced'))
# print(result)
# def checkint(list1):
#     result=[element for element in list1 if isinstance(element,int) ]
#     print(result)
#     # for element in list1:
#     #     if isinstance(element, int):
#     #         result.append(element)
#     # return result



# x=[1,2,3,'a','b']
# result=checkint(x)
# print(result)

# def mode_to_end(lst,element):
#     count=lst.count(element)
#     res=[x for x in lst if x!=element]
#     print("res: ",res)
#     res.extend([element]*count)
#     print(res)
    
# x = mode_to_end([1, 2, 3, 1, 5, 6],1)

# def add_list(list1):
#     return [i+val for i,val in enumerate(list1)]
# res=add_list([5, 4, 3, 2, 1])
# print(res)

# def rmadd(lst,element):
#     if lst:
#         lst.pop(0)
#         lst.append(element)
#         return lst
# x=rmadd([1,2,3,4],6)
# print(x)
# x='hello'
# p=''.join(sorted(x))
# print(p)
# def namerule(names):
#     return ''.join(sorted(name[0] for name in names))
# name=namerule(['Nimu','Amu'])
# print(name)



