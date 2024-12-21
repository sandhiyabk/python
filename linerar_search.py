def linear_search(arr,target):
    for index,value in enumerate(arr):
        if value==target:
            return index
    return -1
arr=[1,2,3,4,5]
target=4
sort=linear_search(arr,target)
if sort!=-1:
    print("present")
else:
    print("not present")
