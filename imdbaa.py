import sys

from bs4 import BeautifulSoup
import requests

resp = requests.get('http://imdb.com/chart/top').text
soups = BeautifulSoup(resp, 'lxml')
sous = soups.prettify()
#print(sous)



###alar = soups.find_all('td',class_='titleColumn')


#pathu = 'toplist.txt'
#sys.stdout = open(pathu,'w')
#for tums in alar:
#    print(tums.text)

alar = soups.find('tbody',class_='lister-list').find_all('tr')

for top in alar:
    nama = top.find('td',class_='titleColumn').a.text
    rata = top.find('td',class_='ratingColumn').strong.text
    yara = top.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
    print(' ( ' + yara  + ' ) ' + nama + " - " + rata)
