import requests
from bs4 import BeautifulSoup

for x in range(15,18):
    url = f'http://jewornotjew.com/profile.jsp?ID={x}'
    #print(url)
    resp = requests.get(url).content
    soup = BeautifulSoup(resp,'html.parser')
    print(str(x) + soup.title.text.rsplit(':',1)[-1])

