import sys
import math

usage = "Usage: python gagecombinator.py <measurement> [precision]"

if 2 > len(sys.argv) > 3:
  print usage
  sys.exit()

arg = 0
precision = 4
if len(sys.argv) == 3:
  try:
    precision = int(sys.argv[2])
  except ValueError:
    print usage
    sys.exit()

try:
  # Translates into an integer with stated precision, to avoid floating point messiness
  arg=math.trunc(float(sys.argv[1])*pow(10,precision+1))
except ValueError:
  print usage
  sys.exit()

list = []

# Subtracts whole numbers, currently in range(1,4)
# Should leave 0.xxxx when finished
for i in range(2,-1,-1):
  comp = pow(10,precision+1)*pow(2,i)
  if arg >= comp:
    arg = arg-comp
    list.append(comp)

# Checks if we can use the 0.050 block
# It's a freebee since there's no .1 tacked on!
dig = int(str(arg)[-1*precision])
if dig >= 5:
  sub = pow(10,precision-1)*5
  arg = arg - sub
  list.append(sub)

# Subtracts greedily, largest available measurement first
# Should leave as close to 0.x000 as possible when finished
for i in range(precision,1,-1):
  if arg > 0:
    dig = int(str(arg)[-1*(i)])
    if dig > 0:
      sub = pow(10,precision)+(pow(10,i-1)*dig)
      if arg >= sub:
        arg = arg-sub
        list.append(sub)

# Splits numbers in the list to account for the remaining 0.x000
# Should leave as close to 0.0000 as possible when finished
if arg >= pow(10,precision):
  dig = int(str(arg)[-1*precision-1])
  sub = pow(10,precision)*dig
  arg = arg - sub
  list.append(sub)
    
form = map((lambda d: 1.0*d/pow(10,precision+1)), list)
print "Please use the below gage blocks:"
mod = "%."+str(precision)+"f"
for i in form:
  print mod % i
left = mod % (1.0*arg/pow(10,precision+1))
if arg > 0:
  print "Combination leaves "+str(left)+"in left over"
