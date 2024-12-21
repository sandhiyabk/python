def foundpos(l,v):
    (found,i)=(False,0)
    while i<len(l):
        if l[i]==v:
            (found,pos)=(True,i)
            break
        i=i+1
    if not found:
        pos=-1
    return(pos)
