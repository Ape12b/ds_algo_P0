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
  if not(telephone in telephones_incoming or telephone in telephones_text):
    possible_telemarketor.append(telephone)

possible_telemarketor.sort()
print("These numbers could be telemarketers: ")
for i in possible_telemarketor:
    print(i)

'''
This implementation has a worst case time complexity of O(n log n) because of the sort operation that happens during printing.
'''