from bs4 import BeautifulSoup
import requests

url = "https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas"
response = requests.get(url)
htmls = response.content
soup = BeautifulSoup(htmls, 'lxml')
# print(soup)

# results = soup.find_all('div', attrs={"class":"textBasedMannualAds})
souptag = soup.find_all('div', class_='article--recommended')

for tagas in souptag:
    print('\n' + tagas.text)




