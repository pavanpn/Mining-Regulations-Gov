#Get Data using Regulations GOV API and save as JSON file
import apiCall

# Main definition
def main():
	# Print Number of Comments
	print apiCall.getNumberOfComments()

# Call main
main()