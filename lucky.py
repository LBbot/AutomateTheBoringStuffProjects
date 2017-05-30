#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
# res = requests.get('http://google.co.uk/search?q=' + ' '.join(sys.argv[1:]))  # Command prompt version instead of next two lines.
search_criteria = input("Input what you want to Google for and this script will open the top results. \n" )
res = requests.get('http://google.co.uk/search?q=' + ' '.join(search_criteria))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")  # Added the parser as per an error message.

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
