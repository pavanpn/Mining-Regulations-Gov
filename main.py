import parseFile
import buildJsonArray
import apiCall
import fileIO
import json

# Main Function
def main():
	
	# Read Files in Data Dir and get Dictionary
	print "Reading Files... \n"
	result_dict = parseFile.getDict()

	# Get Json Array of Text
	print "%d Records. Preparing Data... \n" % ( len(result_dict) )
	textIdDict = buildJsonArray.getTextAndId(result_dict)
	textJsonString = textIdDict["jsonTextList"]
	idList     = textIdDict["idList"]
	textList   = textIdDict["textList"]
	authorList = textIdDict["authorList"]

	# Sentiment Analysis on Text
	print "Calling Sentiment Analysis API... \n"
	sentimentJsonArray = apiCall.getSentimentResults(textJsonString)
	
	# Associate Results with Id
	print "Compiling Results... \n"
	mySentimentDict = {}
	for index in range( len(idList) ):		
		documentId = idList[index]
		mySentimentDict[documentId] = sentimentJsonArray[index]
		mySentimentDict[documentId]["commentText"] = textList[index]
		mySentimentDict[documentId]["author"] = authorList[index]
		
	# Write Sentiment Results to File
	print "Writing to results/sentimentResults.json... \n"
	fileIO.writeJsonFile(mySentimentDict, 'results/sentimentResults.json')
	
	# Ethnicity Analysis on Text
	print "Calling Ethnicity API... \n"
	ethnicityJsonArray = apiCall.getEthnicityResults(authorList)
	
	# Associate Results with Id
	print "Compiling Results... \n"
	myEthnicityDict = {}
	for index in range( len(idList) ):		
		documentId = idList[index]
		myEthnicityDict[documentId]["ethnicity"] = ethnicityJsonArray[index][0]['best']
		myEthnicityDict[documentId]["commentText"] = textList[index]
		myEthnicityDict[documentId]["author"] = authorList[index]

	# Get Gender Given Person Name
	print "Calling Gender API... \n"
	apiCall.getGender(myJsonDict)

	# Print Succcess
	print "Success \n"	

# Call Main	
main()
