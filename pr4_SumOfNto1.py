def sum(n):
    while n >= 0:
        print(n+sum(n-1))
sum(4)