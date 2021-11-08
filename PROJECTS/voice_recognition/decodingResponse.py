import json
 
# Opening JSON file
fileName = './PROJECTS/voice_recognition/response.json'
f = open(fileName,)
 
# returns JSON object as
# a dictionary
data = json.load(f)


# Printing the first Result
print(data['results'][0]['alternatives'][0]['transcript'])

# Printing the second Result
print(data['results'][1]['alternatives'][0]['transcript'])

# Iterating through the json list
for i in data['results']:
    print(i['alternative'][0]['transcript'])

# Printing the start time
print(data['results'][1]['alternatives'][0]['words'][0]['startTime'])

# Converting start time of strings to integer
print(int((data['results'][1]['alternatives'][0]['words'][0]['startTime']).strip('s')))


# Write a program that will return the following response:

for i in data['results'][1]['alternatives'][0]['words']:
    print("Confidence: {:.2f}".format(i['confidence']*100))
    #print(f'Confidence: {i['confidence']*100}')
    print("Word ")
print(data['results'][1]['alternatives'][0]['words'][0]['confidence']*100)

"""
Word 1: Sphinx with confidence of 98.7% starting at 0.2 seconds and ending at 0.5 seconds.
Word 2: Sphinx with confidence of x% starting at 0.2 seconds and ending at 0.5 seconds.
Word 3: Sphinx with confidence of 80% starting at 0.2 seconds and ending at 0.5 seconds.
"""

# Closing file
f.close()