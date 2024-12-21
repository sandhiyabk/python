def min_heap(a,k):
    l=left(k)
    r=right(k)
    if l<len(a) and a[l][0]<a[k][0]:
        smallest=l
    else:
        smallest=k
    if r<len(a) and a[r][0]<a[smallest][0]:
        smallest=r
    if smallest!=k:
        a[k]=a[smallest]=a[smallest],a[k]
        min_heap(a,smallest)
def left(k):
    return 2*k+1
def right(k):
    return 2*k+2
def build_min_heap(a):
    n=int((len(a)//2)-1)
    for k in range(n,-1,-1):
          min_heap(a,k)
a=[10,3,5,2,6]
build_min_heap(a)
print("Minimum Heap is:",a)
    
    
