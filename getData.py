#Get Data using Regulations GOV API and save as JSON file
import apiCall
import sys
import fileIO
import parseFile

# Main definition
def main():
	# Get API KEY as parameter to the function
	if len(sys.argv) > 2:
		API_KEY = sys.argv[1]
		DOCKET_ID = sys.argv[2]
	else:
		print "SYNTAX: getData <API_KEY> <DOCKET_ID>"
		quit()
	# Get Number of Comments
	commentData = apiCall.getLastNComments(API_KEY, DOCKET_ID, str(1000), str(22000) )
	numberofComments = commentData["totalNumRecords"]
	print "Fetching "+numberofComments+" comments."
	# API limit is 1000. Call API 1+numberOfComments/1000 times
	numberofIterations = int(numberofComments/1000)+1
	for index in range (0, numberofIterations, 1):
		PAGE_OFFSET = index * 1000
		commentData = apiCall.getLastNComments(API_KEY, DOCKET_ID, str(1000), str(PAGE_OFFSET) )
		fileIO.writeJsonFile( commentData, "data/file"+str(index) )
	print "Done."
# Call main
main()