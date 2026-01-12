my_array = [7, 12, 9, 4, 11]


minVal=my_array[0]
for i in my_array:
    if i< minVal:
        minVal=i
    
print(minVal)

my_array.sort(reverse=True)
print(my_array)


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1]=my_array[j+1],my_array[j]
            
print(my_array)