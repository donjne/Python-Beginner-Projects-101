import requests
from bs4 import BeautifulSoup

url = 'https://getlinked-ai-hackathon.vercel.app'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all()
title()