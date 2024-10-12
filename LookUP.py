#Hi, if your checking this out the intended way to use the program is To search a HIPSSN number an example
#At the bottem of the code is the HIPSSN number for this program, if your intrested in being added go to
#https://www.sololearn.com/en/compiler-playground/c755qYN1VpsC
import requests

# Configuration
GITHUB_REPO = 'Swift-Sand/HideInPlaneSight'  # Format: username/repo
FILE_PATH = 'List'  # Path in the repo
SEARCH_TERM = input()  # Term you want to search for
def search_in_file():
    """Search for a term in a text file from a public GitHub repository and display matching lines with the next line."""
    try:
        # Construct the URL to fetch the raw content of the file
        url = f'https://raw.githubusercontent.com/{GITHUB_REPO}/main/{FILE_PATH}'
        
        # Fetch the file content
        response = requests.get(url)
        
        if response.status_code == 200:
            file_text = response.text
            lines = file_text.splitlines()
            matching_lines = []
            
            # Search for the term and store matching lines with the next line
            for i in range(len(lines)):
                if SEARCH_TERM in lines[i]:
                    next_line = lines[i + 1] if i + 1 < len(lines) else "No next line available"
                    matching_lines.append((lines[i], next_line))

            # Display results
            if matching_lines:
                print(f'Term "{SEARCH_TERM}" found in the following lines:')
                for i, (matched_line, next_line) in enumerate(matching_lines, start=1):
                    print(f'{i}: {matched_line}')
                    print(f'   Next line: {next_line}')
            else:
                print(f'Term "{SEARCH_TERM}" not found in {FILE_PATH}.')
        else:
            print(f'Error fetching file: {response.status_code} - {response.reason}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    search_in_file()
#Uniqe identifer: HIPSSN-n279917380y
