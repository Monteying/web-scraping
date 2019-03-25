import requests
import csv
from bs4 import BeautifulSoup

row = ['Title', 'Link']

pages = []


with open('chineseinsfbay.csv', 'a', encoding='utf-8', newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerows([row])
    
    # automate change to other pages, number 100 can be any other integers
    for i in range(0,100,15):
        url = 'https://www.chineseinsfbay.com/f/page_viewforum/f_29/start_' + str(i) + '.html'
        pages.append(url)

    for item in pages:
        # Collect and parse first page
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Pull all text from the div class
        title_list = soup.find(class_='forum_left')

        # Pull text from all instances of <a> tag within div class
        title_list_items = title_list.find_all('a', class_='title')
        

        # Print all titles
        for title in title_list_items:
            titles = title.contents[0]
            links = 'https://www.chineseinsfbay.com' + title.get('href')
            
            f.writerow([titles,links])
writeFile.close()
