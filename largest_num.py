
def largest_number(arr):
    large=arr[0]
    for element in arr:
        if element>large:
            large=element
    return large
array=[6,2,3,8]
print(largest_number(array))