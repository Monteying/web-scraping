import requests
import csv
from bs4 import BeautifulSoup

row = ['Title', 'Link', 'Author', 'Time', 'Reply', 'Read']
pages = []


with open('chineseinsfbay.csv', 'a', encoding='utf-8', newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerows([row])
    
    # automate change to other pages, number 100 can be any other integers
    for i in range(0,105,15):
        url = 'https://www.chineseinsfbay.com/f/page_viewforum/f_29/start_' + str(i) + '.html'
        pages.append(url)
    
    # one page per times
    for item in pages:
        
        # Collect and parse page
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Pull all text from the div class
        info_list = soup.find(class_='forum_left')

        # Pull text from all instances of <a> tag within div class
        info_list_title = info_list.find_all('a', class_='title')
        
        # Pull author from all instances of <span> tag within div class
        info_list_author = info_list.find_all('span', class_='author')
        
        # Pull time from all instances of <span> tag within div class
        info_list_time = info_list.find_all('span', class_='time')
        
        # Pull reply count from all instances of <span> tag within div class
        info_list_reply = info_list.find_all('span', class_='reply_count')
        
        # Pull read count from all instances of <span> tag within div class
        info_list_read = info_list.find_all('span', class_='read_count')
        
        
        # Print all titles and links
        for title,author,time,reply,read in zip(info_list_title,info_list_author,info_list_time,info_list_reply,info_list_read):
            titles = title.contents[0]
            links = 'https://www.chineseinsfbay.com' + title.get('href')
            authors = author.contents[0].get_text()
            times = time.contents[0]
            replys = reply.contents[0]
            reads = read.contents[0]
            f.writerow([titles,links,authors,times,replys,reads])
            
writeFile.close()