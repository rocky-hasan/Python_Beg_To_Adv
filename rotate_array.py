# def rotate_arr(arr,d):
#     n=len(arr)
#     if d<0 or d>=n:
#         print("Invalid position")
#     arr_pos=[0]*n
#     for i in range(n):
#         arr_pos[i]=arr[(i+d)%n]
#     return arr_pos
# arr=[1,2,3,4,5]
# d=2
# result=rotate_arr(arr,d)
# print("Array: ", arr)
# print("Rotate array",result)

# Another way
# arr=[1,2,3,4,5]
# d=3

# def split_add(arr,d):
#     fres1=arr[:d]
#     fres2=arr[d:]
#     return fres2+fres1

# result=(split_add(arr,d))
# print(result)

def is_monotonic(x):
    increasing=decreasing=True
    n=len(x)
    for i in range(1,n):
        if x[i]>x[i-1]:
            decreasing=False
        if x[i]<x[i-1]:
            increasing=False
    return increasing or decreasing
        



# Test the function
arr1 = [1, 2, 2, 3] # Monotonic (non-decreasing)
arr2 = [3, 2, 1] # Monotonic (non-increasing)
arr3 = [1, 3, 2, 4] # Not monotonic
print("arr1 is monotonic:", is_monotonic(arr1))
print("arr2 is monotonic:", is_monotonic(arr2))
print("arr3 is monotonic:", is_monotonic(arr3))
