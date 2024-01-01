import math

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

disc=b**2-4*a*c
if disc>0:
    root1=(-b+math.sqrt(disc))/2
    root2=(-b-math.sqrt(disc))/2
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

elif disc==0:
    root=-b/2**a
    print(f"Root : {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(disc)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")

    
