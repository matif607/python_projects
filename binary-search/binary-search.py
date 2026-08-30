""" binary seach is searching for an element in a sorted list where we can minimize 
number of operations and do a faster search by elemenating half of the array at each
turn which is not possible """

import random
import time

l = []
for i in range(10):
  l.append(i + 1)
new_list = l
print(l)
print(new_list)
print(l[4])

def naive_search(l, target):
  for i in range(len(l)):
    if l[i] == target:
      return i
  return -1

def binary_search(l, target, low=None, high=None):
  if low is None:
    low = 0
  
  if high is None:
    high = len(l) - 1
  
  if high < low:
    return -1

  midpoint = (low + high) // 2

  if l[midpoint] == target:
    return midpoint
  elif target < l[midpoint]:
    return binary_search(l, target, low, midpoint - 1)
  else:
    return binary_search(l, target, midpoint + 1, high)


start = time.time()
naive_search(new_list, 6)
end = time.time()
print("naive search finished in", (end - start), "seconds")

start = time.time()
binary_search(new_list, 6)
end = time.time()

print("binary search finished in", (end - start), "seconds")