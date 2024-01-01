num=int(input("Enter Numebr: "))

num_str=str(num)
num_len=len(num_str)
print(num_len)

sum_of_num=0
temp_num=num

while temp_num>0:
    digit=temp_num % 10
    sum_of_num += digit ** num_len
    temp_num //=10
if sum_of_num==num:
    print(f"{num} this is armstrong number")
else:
    print(f"{num} is not an Armstrong number.")



