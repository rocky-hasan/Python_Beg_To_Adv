def add(x,y):
    return x+y
def sub(x,y):
    return x+y
def multiply(x,y):
    return x+y
def division(x,y):
    return x+y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


while True:
    choice=input("Enter Your Choice: ")
    if choice in ('1','2','3','4'):
        try:
            num1=int(input("Enter number1: " ))
            num2=int(input("Enter number2: " ))
        except ValueError:
            print("Invalid Values.Enter Values again")
            continue
        if choice=='1':
            print(add(num1,num2))
        elif choice=='2':
            print(sub(num1,num2))
        elif choice=='3':
            print(multiply(num1,num2))
        elif choice=='4':
            print(division(num1,num2))
        next_calculation = input("Let's do next calculation? (yes/no):") 
        if next_calculation != "yes":
            break
    else:
        print("Invalid Input")