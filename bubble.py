def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(1,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[1,3,2,5,7]
print(bubblesort(arr))
