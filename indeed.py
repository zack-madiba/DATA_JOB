#coding:utf-8
import requests
from bs4 import BeautifulSoup
import datetime


#_____________________________connection a la page indeed_____________________________________________________

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
    url = f'https://fr.indeed.com/emplois?q=data&l=Auvergne-Rh%C3%B4ne-Alpes&start{page}'
    r = requests.get(url,headers)
#    return r.status_code
#print(extract(0))
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

#________________nombre d'annoce sur la premiüre page_____________________
def transform(soup):
    ind = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    #_________________________recuperons les offres de la première page @:) ↓↓↓↓↓
    for item in ind:
        titre = item.find('a').text.strip() # les titres  
        entr = item.find('span', class_='company').text.strip()# les nom d'entreprises
        intitule = item.find('div', class_='summary').text.strip()
        try:
            salaire = item.find('span', class_='salaryText').text.strip() #les salaires
        except:
            salaire = '' 

    print(titre, 'CHEZ : ', entr, 'SALAIRE :', salaire)

    #return len(ind)
#print(transform(c))
c = extract(0)
transform(c)