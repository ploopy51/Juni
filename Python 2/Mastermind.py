# main.py
import random
k = 0
i = 0
o = 0
a = random.randint(0,4)
b = random.randint(0,4)
c = random.randint(0,4)
d = random.randint(0,4)
b = [a,b,c,d]
while 0 < 4:
  k = 0
  i = 0
  o = 0
  l = input("give me a four number sequence")
  tempb = ""
  templ = ""
  for number in l:
    if int(number) == b[i]:
      o = o + 1
    else:
      templ += (number)
      tempb += str(b[i])
    i += 1
  i = 0
  for number in templ:
    if str(number) in tempb:
      k += 1
      tempb = tempb[:i] + tempb[i + 1:] 
    i += 1
  if o == 4:
    print("you are, a MASTERMIND")
    break
  else:
    print("you have gotten " + str(o) + " correct")
    print("you have gotten " + str(k) + " close")
    print("you have gotten" +  str(4 - (o + k)) + "wrong")
