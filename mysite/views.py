from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from .forms import QuizForm



gpu_page = requests.get("https://www.newegg.com/p/pl?Submit=StoreIM&Category=38&Depa=1&Order=3")
cpu_page = requests.get("https://www.newegg.com/Processors-Desktops/SubCategory/ID-343?Tid=7671&Order=4")
motherboard_page = requests.get("https://www.newegg.com/p/pl?Submit=StoreIM&Category=20&Depa=1&Order=3")
monitors_page = requests.get("https://www.newegg.com/p/pl?Submit=StoreIM&Category=19&Depa=133&Order=3")

#Web scrapes for gpu info on newegg.com
def gpu_info():
    if (gpu_page):
        soup = BeautifulSoup(gpu_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
    for index in item[0:10]:
        titles = index.find(class_="item-title").get_text()
        prices = index.find(class_="price").get_text()
        print(titles)
        print(prices)

#Web scrapes for cpu info on newegg.com
def cpu_info():
    if (cpu_page):
        soup = BeautifulSoup(cpu_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
        for index in item[0:10]:
            titles = index.find(class_="item-title").get_text()
            prices = index.find(class_="price").get_text()  
            print(titles)
            print(prices)

#Web scrapes for motherboard info on newegg.com
def motherboard_info():
    if (motherboard_page):
        soup = BeautifulSoup(motherboard_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
        for index in item[0:10]:
            items_data = []
            titles = index.find(class_="item-title").get_text()
            prices = index.find(class_="price").get_text()
            items_data.append(titles)
            items_data.append(prices)
            # print(items_data)
            print(titles)
            print(prices)

#Web scrapes for monitors on newegg.com
def monitor_info():
    if (monitors_page):
        soup = BeautifulSoup(monitors_page.content, 'html.parser')
        top_items = soup.find(class_="list-wrap")
        item = top_items.find_all(class_="item-cell")
        for index in item[0:10]:
            titles = index.find(class_="item-title").get_text()
            prices = index.find(class_="price").get_text()
            print(titles)
            print(prices)


#Renders the homepage and makes the decision on which function to call when the user selects the desired part from the dropdown menu
def homepage(request):
    context = {}
    context['form'] = QuizForm()
    if request.GET:
        initial_fetch = request.GET['pc_parts_choice']
        if request.GET['pc_parts_choice'] == '1':
            print(gpu_info())
        elif request.GET['pc_parts_choice'] == '2':
            print(cpu_info())
        elif request.GET['pc_parts_choice'] == '3':
            print(motherboard_info())
        elif request.GET['pc_parts_choice'] == '4':
            print(monitor_info())
    return render(request, "welcome.html", context)





