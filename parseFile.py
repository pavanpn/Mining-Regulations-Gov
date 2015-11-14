import json
import fileIO
import glob

# Read Files in Directory
def readFiles(myPath):
	myFileNames =  	glob.glob(myPath)
	result_dict = {}
	for file in myFileNames:
		# Form dictionary from input files
		myDict = fileToDict ( file )
		result_dict = dict(myDict.items() + result_dict.items())
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
def getDict(myPath):
	myDict = readFiles(myPath)
	return myDict
