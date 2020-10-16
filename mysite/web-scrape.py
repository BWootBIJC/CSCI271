import requests
from bs4 import BeautifulSoup


gpu_page = requests.get("https://www.newegg.com/p/pl?Submit=StoreIM&Category=38&Depa=1&Order=3")
soup = BeautifulSoup(gpu_page.content, 'html.parser')

#Stores all html code for every gpu from the newegg url.
top_items = soup.find(class_="list-wrap")

#Stores all html code for each individual gpu from the newegg url
item = top_items.find_all(class_="item-cell")

#Stores the html code for the title of the first gpu
#item_one_title = item.find(class_="item-title").get_text()
#item_one_price = item[0].find(class_="price").get_text()

def get_title():
    for index in item:
        #empty_array = []
        titles = index.find(class_="item-title").get_text()
        prices = item[0].find(class_="price").get_text()
        print(titles)
        print(prices)
print(get_title())

