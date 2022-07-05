def rev(g):
    g=int(g)
    l=len(str(g))
    reminder = int(g%10)
    value = int(g%10 * 10**(l-1))
    #print('value:', value)
    new = (g-reminder)/10
    
    if new<=0:
        return g
    l = new
    return(value+rev(new))
    
print(rev(89076584))