import random
import string
#HIPSSN-Q572096731G
#SUPER IMPORTENT
#BEFORE USE GO TO
#https://github.com/Swift-Sand/HideInPlaneSight/blob/main/README
#for instructions
#SUPER IMPORTANT
print("IMPORTENT please read the comments in code")
# Generate a random number between 1 and 999999999
number = str(random.randint(1, 999999999))  # Fixed 'sr' to 'str'

# Randomly choose a letter from all the ascii_letters
randomLetter = str(random.choice(string.ascii_letters))  # Added closing parenthesis
randomLetter2 = str(random.choice(string.ascii_letters))  # Added closing parenthesis

# Print the combined result
ser = "HIPSSN-" + randomLetter + number + randomLetter2
#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
import requests
import json
import base64

# Replace with your GitHub username
GITHUB_USERNAME = 'Swift-Sand'
# Replace with your GitHub repository name
REPO_NAME = 'HideInPlaneSight'
# Replace with your personal access token
ACCESS_TOKEN = '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'
# Name of the file to modify
FILE_NAME = 'List'

# Variables to add
variable1 =   ser
variable2 = input()  # Second variable

# URL to get the file content
url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{FILE_NAME}'

# Get the current content of the file
response = requests.get(url, headers={'Authorization': f'token {ACCESS_TOKEN}'})

if response.status_code == 200:
	# Decode the content from base64
	file_info = response.json()
	current_content = base64.b64decode(file_info['content']).decode('utf-8')
	
	# Append new variables to the current content
	new_content = current_content + f"\n{variable1}\n{variable2}"

	# Prepare the updated file content
	update_payload = {
		"message": "Update file with new variables",
		"content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
		"sha": file_info['sha'],  # Required to update the file
		"branch": "main"  # Change if you are using a different branch
	}

	# Make the request to update the file
	update_response = requests.put(url, headers={'Authorization': f'token {ACCESS_TOKEN}'}, data=json.dumps(update_payload))

	# Check the response from the update request
	if update_response.status_code == 200:
		print("File updated successfully!")
	else:
		print(f"Failed to update file: {update_response.status_code} - {update_response.text}")
else:
	print(f"Failed to retrieve file: {response.status_code} - {response.text}")
print("Your projects unique identifier is") 
print(ser)
print("don't forget to paste that in! ")
print("for a example this projectS unige identifyer is: HIPSSN-Q572096731G")
