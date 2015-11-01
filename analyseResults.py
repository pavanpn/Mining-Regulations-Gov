import fileIO
import json
import pprint
import re
import requests

# Count sentiment categories and print them
def printSentiments(myJsonDict):
	# Counter for 3 categories
	postitiveCounter = 0
	negativeCounter  = 0
	neutralCounter   = 0
	for key, value in myJsonDict.iteritems():
		result = value['result']
		if ( result  == 'Negative' ):
			negativeCounter += 1
		elif (result == 'Positive'):
			postitiveCounter += 1
		else:
			neutralCounter += 1
	# Print results
	print "Positive: %d, Negative: %d, Neutral: %d \n" % (postitiveCounter, negativeCounter, neutralCounter)


# Count sentiment categories and print them
def printGenderSentiments(myJsonDict):
	# Counter for 6 categories
	m_postitiveCounter = 0
	m_negativeCounter  = 0
	m_neutralCounter   = 0
	
	f_postitiveCounter = 0
	f_negativeCounter  = 0
	f_neutralCounter   = 0
	
	for key, value in myJsonDict.iteritems():
		result = value['result']
		gender = value['gender']

		if ( result  == 'Negative' and gender == 'male'):
			m_negativeCounter += 1
		elif ( result  == 'Negative' and gender == 'female'):
			f_negativeCounter += 1
		elif ( result  == 'Positive' and gender == 'male'):
			m_positiveCounter += 1
		elif ( result  == 'Positive' and gender == 'female'):
			f_positiveCounter += 1
		elif ( result  == 'Neutral' and gender == 'male'):
			m_neutralCounter += 1
		elif ( result  == 'Neutral' and gender == 'female'):
			f_neutralCounter += 1
	# Print results
	print "Male:\n--------\n Positive: %d, Negative: %d, Neutral: %d \nFemale:\n--------\nPositive: %d, Negative: %d, Neutral: %d \n" % (m_postitiveCounter, m_negativeCounter, m_neutralCounter, f_postitiveCounter, f_negativeCounter, f_neutralCounter)

		
# Main function
def main():
	# Read output file and convert to dictionary
	myJsonArray = fileIO.readJsonFile('results/sentimentResults.json')
	myJsonDict   = json.loads(myJsonArray)
	# Send dict to print sentiments
	# printSentiments(myJsonDict)
	
# Call Main	
main()


