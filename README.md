# Mining-Regulations-Gov
Sentiment, Gender and Ethnicity based Analysis of Comments on data from Regulations.gov

# Setup
This repository consists of : 
- getData.py        : Uses Regulations.gov API to retrieve data given API_KEY and DOCKET_ID.
```
python getData.py <API_KEY> <DOCKET_ID>
```
- main.py           : Reads data, cleans data and calls APIs for sentiment analysis, gender identification from first name and ethniciy identification from full name.
```
python main.py
```
- data folder       : Results of getData.py. Contains comments retrieved via Regulations.gov API
- results folder    : Contains results of analysis as JSON files
- analyseResults.py : Prints a quick summary of results of analysis.

# Sample Results for Regulations.gov
"docketId":"ICEB-2015-0002",
"docketTitle":"Improving and Expanding Training Opportunities for F-1 Nonimmigrant Students with STEM Degrees; Cap-Gap Relief for All F-1 Students With Pending H-1B Petitions and Change of Status Requests"

- Positive: 15149
- Negative: 5420
- Neutral: 1997
- Male: Female ratio = 3:1

# TO DO
- Gender API is limited to 1000 calls
- Ethnnicity API has very high latency
- Need to use this command currently to analyse gender 
```
grep -o 'None' genderAPI.csv | wc -l
```