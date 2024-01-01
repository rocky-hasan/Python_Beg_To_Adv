def is_happy(num):
    seen=set()
    while num!=1 and num not in seen:
        seen.add(num)
        num=sum(int(i)**2 for i in str(num))
    return num==1

num=int(input("Enter A Number: "))

if is_happy(num):
    print(num)
else:
    print("not happy number")