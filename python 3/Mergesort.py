# main.py

def merge(list1,list2):
  sort = []
  pointa = 0
  pointb = 0
  while pointa < len(list1) and pointb < len(list2):
    if list1[pointa] < list2[pointb]:
      sort.append(list1[pointa])
      pointa += 1
    else:
      sort.append(list2[pointb])
      pointb += 1
      
  while pointa < len(list1):
    sort.append(list1[pointa])
    pointa += 1
    
  while pointb < len(list2):
    sort.append(list2[pointb])
    pointb += 1
  return sort

def mergesort(numbers):
  n = len(numbers)
  if n <= 1:
    return numbers
    
  a = mergesort(numbers[:n//2])
  b = mergesort(numbers[n//2:])
  
  return merge(a,b)
print(mergesort([9,1,3,8,7]))
  
  
  
  
#big o: overall time complexity = n*logn
