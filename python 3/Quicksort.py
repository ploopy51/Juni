# main.py
import random
def partition(numbers,pivot):
  lesslist = []
  greaterlist = []
  equallist = []
  for n in numbers:
    if n > pivot:
      greaterlist.append(n)
    elif n < pivot:
      lesslist.append(n)
    else:
      equallist.append(n)
  return lesslist,equallist,greaterlist

def quicksort(numbers):
  lesslist = []
  greaterlist = []
  equallist = []
  if len(numbers) <= 1:
    return numbers
  pivot = random.choice(numbers)
  less, eq, great = partition(numbers,pivot)
  
  sortless = quicksort(less)
  sortgreater = quicksort(great)
  return(sortless + eq + sortgreater)

print(quicksort([9,3,1,7,4,8]))
    
      
  
#big o :best  n*log(n), worst: n^2
