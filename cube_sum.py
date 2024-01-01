def cube_sum(x):
    sum=[x**3 for x in range (1,x+1)]
    return sum


x=int(input("Enter number : "))
if x<0:
    print("Enter positive number")
else:
    result=cube_sum(x)
print(result)