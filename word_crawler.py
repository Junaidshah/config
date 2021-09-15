import requests
from bs4 import BeautifulSoup
from collections import Counter

url = requests.get("http://localhost")

soup = BeautifulSoup(url.content, features="html.parser")

# find all text under p tags from the html, strip out just the text and join them.
joined_text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

# go over the text, split it out to a list and pass that to counter.
item_counter = Counter((x for every_word in joined_text for x in every_word.split()))
print(f'{item_counter}')