"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
duration = 0
index = 0
for i in range(len(calls)):
    if int(calls[i][-1]) > duration:
        index = i
        duration = int(calls[i][-1])
    
print(f"{calls[index][0]}, {calls[index][1]} spent the longest time, {duration} seconds, on the phone during September 2016.")


'''
Output:
output
89071 50880, (04546)388977 spent the longest time, 4617 seconds, on the phone during September 2016.
'''

'''
The algorithm runs in O(n) where n is proportional to the number of rows in calls list.
'''