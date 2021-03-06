'''
Solution #1 (too many lines)

"""
Accepting the inputs.
"""
n = int(input())
l = input().split(' ')

"""
Sorting the list.
"""
# 2 3 1 5
# check 3 times to make sure its proper.
for i in range(n - 2):
  # 4 numbers, 1-3
  for j in range(n - 2):
    if l[j + 1] < l[j]: # if 3 < 2
      temp = l[j] # temporarily stores 2
      # swaps the numbers
      l[j] = l[j + 1] # 2 = 3
      l[j + 1] = temp # 3 = 2

"""
Finding the missing number.
"""
m = None;
for i in range(n - 1):
  if not i + 1 == int(l[i]):
    m = i + 1
    break

'''


'''
Better Solution
'''

# Accepting the inputs.
n = int(input("Amount of numbers: "))
l = input("List of numbers (Space between num): ").split(' ')

# Getting the sum from 1 to n.
s = 0;
for i in range(1, n + 1):
  s += i

# Getting the sum of list.
s2 = 0;
for i in l:
  s2 += int(i)

# Subtracting both sums.
m = s - s2

# Printing out the missing number.
print(m)
