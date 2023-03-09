from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.legit.ng/latest/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_='c-article-card-no-border')

with open('scraped.csv', 'w', newline='') as f:
    thewriter = writer(f)
    header = ['Title','Headlines','Time','Image']
    thewriter.writerow(header)
    for i in lists:
        title = i.find('a', class_='c-article-card-no-border__headline').attrs['href']
        headlines = i.find('span', class_='c-article-card-no-border__headline-hover-inner').text
        time = i.find('time', class_='c-article-info__time--clock').text
        image = i.find('img', class_='lazyload thumbnail-picture__img').attrs['src']
        
        data = [title, headlines, time, image]
        print(data)
        thewriter.writerow(data)
    
