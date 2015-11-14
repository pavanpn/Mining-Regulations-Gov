import requests
import json 
import itertools
import math
import fileIO
import re
import urllib

# Get Number of Comments on regulation, given API_KEY and DOCKET_ID
def getLastNComments(API_KEY, DOCKET_ID, LIMIT, END_NUMBER):
	# Call the URL and get the number of comments
	getRegulationUrl = "http://api.data.gov:80/regulations/v3/documents.json?api_key="+API_KEY+"&dktid="+DOCKET_ID+"&rpp="+LIMIT+"&po="+END_NUMBER
	response = urllib.urlopen(getRegulationUrl)
	commentData = json.loads(response.read())
	# Return commentData
	return commentData

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
		myOutString = str(myName)+","+str(myGender)
		fileIO.writeFile(myOutString, 'results/genderAPI.csv')
	
# Get Gender by First Name
def getGender(authorList):
	counter     = 0
	apiLimit    = 0
	apiString   = ""
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
		# Check for API Limit
		if apiLimit > 900:
			break
		# Set limit to 10 names per call
		if (counter == 9):
			# Call the API and write results to File
			results = callGenderAPI(apiString)
			myJsonDict = processResults(results, myNameList)
			print "Processing \n"
			# Reset counters after 10
			apiString = ""
			counter   = 0
			apiLimit += 10 
			myDocIdList = []
			myNameList = []
	# Call API last time for remaining names
	if apiString != "":
		callGenderAPI(apiString)
	# Write Gender Results to File
	print "Writing to results/genderResults.json... \n"
	fileIO.writeJsonFile(myJsonDict, 'results/genderResults.json')
