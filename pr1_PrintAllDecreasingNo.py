#print al decreasing number from n to 0

def pri(n):
    if n==0:
        exit()
    print(n)
    n-=1
    pri(n)
print(pri(12))