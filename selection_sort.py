def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
arr=[1,7,4,5,3,2]
selection_sort(arr)
print(arr)
            
            
