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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
def prefix(number):
    '''
    Function to extract the prefix from a phone number
    '''
    if number[0] == "(":
        temp = ""
        for i in number:
            temp += i
            if i == ")":
                return temp
    elif number[:3] == "140":
        return("140")
    elif number[0] in ["7", "8", "9"]:
        return(number[:4])
    
area_called = {}
for i in calls:
    if i[0][:5] == "(080)":
        area_called[prefix(i[1])] = 1

numbers_called = list(area_called.keys())
numbers_called.sort()

print("The numbers called by people in Bangalore have codes:")
for i in numbers_called:
    print(i)
    
'''
Output:
The numbers called by people in Bangalore have codes:
(022)
(040)
(04344)
(044)
(04546)
(0471)
(080)
(0821)
7406
7795
7813
7829
8151
8152
8301
8431
8714
9008
9019
9035
9036
9241
9242
9341
...
9844
9845
9900
9961
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
'''
'''
This implementation has a worst case time complexity of O(n log n) because of the sort operation that happens during printing.
'''

# Part B
bangalore_calls = 0
other_calls = 0
    
area_called = {}
for i in calls:
    if i[0][:5] == "(080)":
        if i[1][:5] == "(080)":
            bangalore_calls += 1
        else:
            other_calls += 1

print(f"{round(bangalore_calls / (bangalore_calls + other_calls) * 100, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

'''
Output:
24.81 percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.
'''

'''
The implementation is O(n) in complexity. It is proportional to the length of the calls list.
'''