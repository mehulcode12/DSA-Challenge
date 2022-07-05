#print al decreasing number from n to 0
s = 0
def asc(n):
    global s
    s+=1
    print(s)
    if n == s:
        return n
    asc(n+1)
asc(5)
