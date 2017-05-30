import requests, time, webbrowser, bs4

url = 'http://www.reddit.com/'
while True:
    try:
        res = requests.get(url)
        res.raise_for_status()
        break
    except requests.exceptions.HTTPError:
        if res.status_code != 429:
            raise
        print("Server says too many requests. Trying again in 5 seconds.")
        time.sleep(5)

soup = bs4.BeautifulSoup(res.text, "html.parser")
entryLink = soup.select('a[class="title may-blank outbound"]')
for link in entryLink:
    print(link.get('href'))
    #webbrowser.open(link.get('href'))
