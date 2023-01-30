import requests
from bs4 import BeautifulSoup

# Make sure user enters 'a' or 'c'
lvl = 'e'
while lvl != 'a' or lvl != 'c':
    lvl = input("Enter 'a' for ATP matches or 'c' for Challenger matches.\n")
    if lvl == 'a' or lvl == 'c':
        break

if lvl == "a":
    url = 'https://www.atptour.com/en/scores/current/'
else:
    url = 'https://www.atptour.com/en/scores/current-challenger/'

html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

# results = s.find(id=id="lastEventsPlayedStandAloneNoSlider")

results = s.select('#lastEventsPlayedStandAloneNoSlider > div > div > div.rsContent.rsActiveSlide > div > table > tbody > tr > td.title-content')
print(results[0].getText())

# tournament = results.find_all('a', class_='tourney-title')

# print(tournament[0].text)
