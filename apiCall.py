import requests
import json 
import itertools
import math
import re

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
def processResults(results, myNameList):
	for index in range( len(results) ):	
		myGender = results[index]['gender'] 
		myName = myNameList[index]
		writefile(myName+","+myGender, 'results/genderAPI.csv')
	
# Get Gender by First Name
def getGender(authorList):
	counter = 0
	apiString = ""
	myNameList  = []
	# Preprocess the data and use only
	for index in range ( len(authorList) ):
		counter += 1
		fname = authorList[index]
		myNameList.append(fname)
		# Get only the first name
		name = fname.split(' ')[0].lstrip(' ')
		re.sub(r'\W+', '', name)
		# Generate string in required API format
		apiString = apiString + "name[%d]=%s&" % (counter, name)
		# Set limit to 10 names per call
		if (counter == 9):
			# Call the API and write results to File
			results = callGenderAPI(apiString)
			myJsonDict = processResults(results, myNameList)
			print "Processing \n"
			# Reset counters after 10
			apiString = ""
			counter = 0
			myDocIdList = []
			myNameList = []
	# Call API last time for remaining names
	if apiString != "":
		callGenderAPI(apiString)
	# Write Gender Results to File
	print "Writing to results/genderResults.json... \n"
	fileIO.writeJsonFile(myJsonDict, 'results/genderResults.json')
