import json

# Write inputString to JSON myFilename
def writeJsonFile(inputString, myFilename):
	with open(myFilename, 'w') as outfile:
		json.dump(inputString, outfile)
    
# Read from JSON myFilename    
def readJsonFile(myFilename):
	myFileObject = open (myFilename, 'r')
	myJsonStr    = myFileObject.read()
	return myJsonStr
	
# Write inputString to myFilename
def writeFile(inputString, myFilename):
	with open(myFilename, 'a') as outfile:
		outfile.write(inputString)
