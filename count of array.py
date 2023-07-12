def count_array(arr):
    count_array=0
    maximum=float("-inf")
    for i in arr:
        if i > maximum:
            maximum=i
    for i in arr:
        if i == maximum:
            count_array+=1
    return len(arr)-count_array
print(count_array(list(map(int,input().split()))))


            
