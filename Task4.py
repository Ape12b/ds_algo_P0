"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
telephones = {}
telephones_incoming = {}
telephones_text = {}

for i in calls:
    telephones[i[0]] = 1
    telephones_incoming[i[1]] = 1

for i in texts:
    telephones_text[i[0]] = 1
    telephones_text[i[1]] = 1

possible_telemarketor = []
for telephone in telephones:
  if not(telephone in telephones_incoming or telephone in telephones_text) and telephone[:3] != "140":
    possible_telemarketor.append(telephone)

possible_telemarketor.sort()
print("These numbers could be telemarketers: ")
for i in possible_telemarketor:
    print(i)

'''
These numbers could be telemarketers: 
(022)37572285
(022)65548497
(022)68535788
(022)69042431
(040)30429041
(044)22020822
(0471)2171438
(0471)6579079
(080)20383942
(080)25820765
(080)31606520
(080)40362016
(080)60463379
(080)60998034
(080)62963633
(080)64015211
(080)69887826
(0821)3257740
74064 66270
78291 94593
87144 55014
90351 90193
92414 69419
94495 03761
97404 30456
97407 84573
97442 45192
99617 25274
'''
'''
This implementation has a worst case time complexity of O(n log n) because of the sort operation that happens during printing.
'''