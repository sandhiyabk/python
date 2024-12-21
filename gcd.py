def gcd(m,n):
    m=int(input("enter m"))
    n=int(input("enter n"))         
    fm=[]
    for i in range(1,m+1):
        if(m%i==0):
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if(m%j==0):
            fm.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
        print(cf[-1])
            
