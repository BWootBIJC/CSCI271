import requests
from bs4 import BeautifulSoup


gpu_page = requests.get("https://www.newegg.com/p/pl?Submit=StoreIM&Category=38&Depa=1&Order=3")
cpu_page = requests.get("https://www.newegg.com/Processors-Desktops/SubCategory/ID-343?Tid=7671&Order=4")
motherboard_page = requests.get("https://www.newegg.com/p/pl?Submit=StoreIM&Category=20&Depa=1&Order=3")
monitors_page = requests.get("https://www.newegg.com/p/pl?Submit=StoreIM&Category=19&Depa=133&Order=3")


def gpu_info():
    if (gpu_page):
        soup = BeautifulSoup(gpu_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
    elif (cpu_page):
        soup = BeautifulSoup(cpu_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
    elif (motherboard_page):
        soup = BeautifulSoup(motherboard_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
    elif (monitors_page):
        soup = BeautifulSoup(monitors_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
    for index in item:
        titles = index.find(class_="item-title").get_text()
        prices = index.find(class_="price").get_text()
        #prices[:10]
        print(titles)
        print(prices)


print(gpu_info())