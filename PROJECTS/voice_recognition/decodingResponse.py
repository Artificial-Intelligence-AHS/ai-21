import json
 
# Opening JSON file
fileName = './PROJECTS/voice_recognition/response.json'
f = open(fileName,)
 
# returns JSON object as
# a dictionary
data = json.load(f)

print("-"*20)
# Printing the first Result
print(data['results'][0]['alternatives'][0]['transcript'])
print("-"*20)
# Printing the second Result
print(data['results'][1]['alternatives'][0]['transcript'])
print("-"*20)
# Printing the start time
print(data['results'][1]['alternatives'][0]['words'][0]['startTime'])
print("-"*20)
# Converting start time of strings to integer
print(int((data['results'][1]['alternatives'][0]['words'][0]['startTime']).strip('s')))
print("-"*20)
# Write a program that will return the following response:

count = 1
for i in data['results'][1]['alternatives'][0]['words']:
    print("Word #{}: \"{}\" with a confidence: {:.2f}".format(count,i['word'], i['confidence']*100))
    #print(f'Confidence: {i['confidence']*100}')
    count += 1

"""
Word 1: Sphinx with confidence of 98.7% starting at 0.2 seconds and ending at 0.5 seconds.
Word 2: Sphinx with confidence of x% starting at 0.2 seconds and ending at 0.5 seconds.
Word 3: Sphinx with confidence of 80% starting at 0.2 seconds and ending at 0.5 seconds.
"""

# Closing file
f.close()