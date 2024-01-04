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
call_len = {}
for call in calls:
    try:
        call_len[call[0]] += int(call[-1])
    except:
        call_len[call[0]] = 0
    try:
        call_len[call[1]] += int(call[-1])
    except:
        call_len[call[1]] = 0
    
Keymax = max(zip(call_len.values(), call_len.keys()))[1]
print(Keymax)
print(f"{Keymax} spent the longest time, {call_len[Keymax]} seconds, on the phone during September 2016.")


'''
Output:
(080)33251027 spent the longest time, 90346 seconds, on the phone during September 2016.
'''

'''
The algorithm runs in O(n) where n is proportional to the number of rows in calls list.
'''