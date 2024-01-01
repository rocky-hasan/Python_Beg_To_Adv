# 8^1 +9^2 = 8 + 81 = 89 (make this)

def is_disatium(num):
 str_num=str(num)
 digit_num=sum(int(i)**(index+1) for index,i in enumerate(str_num))
 return digit_num==num
 


disarium_number=[num for num in range(1,101) if is_disatium(num)] 
print("Disarium numbers between 1 and 100:")
for num in disarium_number:
 print(num, end=" | ")