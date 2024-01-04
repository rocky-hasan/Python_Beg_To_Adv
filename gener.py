# class DivideBySeven:
#     def __init__(self,x) -> None:
#         self.x=x
#     def generatenumber(self):
#         for num in range(self.x+1):
#             if num % 7 == 0:
#                 yield num
# result=DivideBySeven(50).generatenumber()
# for num in result:
#     print(num )

def DivideBySeven(num):
    for i in range (num+1):
        if i%5==0 and i%7==0:
            yield i


try:
    n=int(input("Enter Number: "))
    result=DivideBySeven(n)
    print(','.join(map(str,result)))
except ValueError:
    print("Enter Valid number!!!")