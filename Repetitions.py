l = list(input()) # list variable
r = 1 # repeats variable
t = 1 # temp variable

# for i = 1, to length of l
for i in range(1, len(l)):
  if l[i] == l[i-1]: # if same character
    t = t + 1 # temp += 1
    if i == len(l) - 1 and t > r: # if last element, and t > r
      r = t # repeat = temp
  else: # not same character
    if t > r: # if temp > repeat
      r = t # repeat = temp
    t = 1 # reset temp

print(r) # print out the max repeats
