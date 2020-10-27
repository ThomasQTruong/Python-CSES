n = input() # length of array
l = input().split(' ') # array

# 3 2 5 1 7
# for 0 to 5
for i in range(1, len(l)):
  # if 3 > 2
  if l[i-1] > l[i]:
    t = l[i] # t = 2
    l[i] = l[i-1] # 2 = 3
    l[i-1] = t # 3 = 2
    # isnt working
    if i > 1: # i = 2 and up
      i = i - 2 # recheck

print(l)
