n = int(input("Please enter the value of n: "))

while n > 1:
  print(str(int(n)), end = ' ')
  if(n % 2 == 1): # is an odd.
    n = n * 3 + 1
  else:
    n = n / 2

print(str(int(n)), end = ' ')
