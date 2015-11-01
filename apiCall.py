import requests
import json 
import itertools
import math

# Get Sentiment Value from API
def getSentimentResults(jsonString):
	url = 'http://sentiment.vivekn.com/api/batch/'
	response = requests.post(url, data=jsonString)
	return response.json()
	
# Get Ethnicity from TextMap API	
def getEthnicityResults(authorList):
	url = 'http://www.textmap.com/ethnicity_api/api'
	curList0 = json.dumps(authorList[0:2])
	response1 = requests.post(url, data=curList0)
	print "Len: %d" %(len(response.json()))
	return response1.json()
	
# Call API from Genderize
def callGenderAPI(inputString):
	url = "https://api.genderize.io/?%s" % (inputString)
	response = requests.request('GET',url)
	return response.json()

# Write Gender Results to File
def processResults(results, myJsonDict, myDocIdList, myNameList):
	
	for index in range( len(results) ):	
		myDocId = myDocIdList[index]
		myGender = results[index]['gender'] 
		myName = myNameList[index]
		writefile(myDocId+","+myGender+","+myName, 'results/genderAPI.csv')
	
# Get Gender by First Name
def getGender(inputJsonDict):
	myJsonDict = inputJsonDict
	counter = 0
	apiString = ""
	myDocIdList = []
	myNameList  = []
	# Preprocess the data and use only
	# 10 names per API call
	for key, value in myJsonDict.iteritems():
		counter += 1
		fname = value['author']
		name = fname.split(' ')[0].lstrip(' ')
		re.sub(r'\W+', '', name)
		myDocIdList.append(key)
		myNameList.append(key)
		if name == ":":
			print "\n\n\n ERR \n\n", fname, "\n"
		apiString = apiString + "name[%d]=%s&" % (counter, name)
		if (counter == 9):
			counter = 0
			results = callGenderAPI(apiString)
			myJsonDict = processResults(results, myJsonDict, myDocIdList, myNameList)
			apiString = ""
			print "Processing \n"
			myDocIdList = []
			myNameList = []
	# Call API last time for remaining names
	if apiString != "":
		callGenderAPI(apiString)
	# Write Gender Results to File
	print "Writing to results/genderResults.json... \n"
	fileIO.writeJsonFile(myJsonDict, 'results/genderResults.json')
