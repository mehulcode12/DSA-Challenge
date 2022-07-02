#learnt binary search
#upeer bound and middle

#solving same question as of day1
pos = -1
def search(list,n):
  i = 0
  while i <len(list):
    if list[i] ==n:
      globals()['pos'] = 1
      return True
    i = i+1
  return False

print(search([23,34,45,67,89],45))
