import json
import fileIO

# Read File
def readFiles():
	# Form dictionary from input files
	dict0 = fileToDict ( 'data/documents0.json' )
	dict1 = fileToDict ( 'data/documents1000.json' )
	dict2 = fileToDict ( 'data/documents2000.json' )
	dict3 = fileToDict ( 'data/documents3000.json' )
	# Final dictionary
	result_dict = dict(dict0.items() + dict1.items() + dict2.items() + dict3.items() )
	return result_dict

# Convert to Dictionary
def fileToDict( myFilename ):
	# Read data and convert to dictionary
	myJsonStr    = fileIO.readJsonFile(myFilename)
	myJsonDict   = json.loads(myJsonStr)
	# Extract only document portion
	myJsonDictData  = myJsonDict["documents"]
	# Return new dictionary with key as 'documentId'	
	myJsonFinalDict = {}
	for index in range( len(myJsonDictData) ):		
		myJsonDictTitle  = myJsonDictData[index]["documentId"]
		myJsonFinalDict [myJsonDictTitle] = myJsonDictData[index]
	return myJsonFinalDict

# Get Dictionary
def getDict():
	myDict = readFiles()
	return myDict
