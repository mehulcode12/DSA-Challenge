#learnt binary search
#upeer bound and middle

#solving same question as of day1
card = [90,78,67,45,34,23,5,1,-99]
query = 1
pos = -1

def locate_card(card,query):
  upper_bound = len(card)-1
  lower_bound = 0
  while lower_bound <= upper_bound:
    mid = lower_bound+upper_bound // 2
    if mid == query:
      globals()['pos'] == mid
    else:
      if mid > upper_bound:
        upper_bound == mid +1
      else:
        lower_bound == mid - 1
  return False

if locate_card(card,query):
  print("found at: ", pos)
else:
  print("not found")
