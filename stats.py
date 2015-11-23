# alculate the sum of the values in a text file,
# formatted as one floating point value per line.

import sys

values = []
for line in open(sys.argv[1]):
   value = float(line)
   values.append(value)

total = sum(values)

print len(values), 'values were read in'
print 'The sum of the input values is:', total
