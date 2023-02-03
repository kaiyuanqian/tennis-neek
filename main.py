import requests
from bs4 import BeautifulSoup

url = 'http://www.espn.com/tennis/dailyResults'

html = requests.get(url)

s = BeautifulSoup(html.text, 'lxml')

all_scores = s.find('div', class_='span-4')

num = len(all_scores.find_all('div', class_='scoreHeadline'))

i = 0


while i < num:
    tournament_names = all_scores.find_all('div', class_='scoreHeadline')
    name = tournament_names[i].a.text
    print(name)
    
    tournament_round = all_scores.find_all('div', class_='matchTitle')
    round = tournament_round[i].text
    print(round)
    
    print()
    i+=1
    


# results = s.select('#lastEventsPlayedStandAloneNoSlider > div > div > div.rsContent.rsActiveSlide > div > table > tbody > tr > td.title-content')
# print(results[0].getText())

# tournament = results.find_all('a', class_='scoreHeadline')

