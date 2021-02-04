import requests
from bs4 import BeautifulSoup
import unicodedata
import re

print("ha")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

URL = 'https://prisguiden.no/kategorier/baerbar-pc?p=gaming-pc'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

items = []

#print(soup.contents)

for a in soup.find_all("div", class_="category-result-item product"):
    link = re.findall("href=[\"\'](.*?)[\"\']", str(a))
    #title = re.findall('<img alt=\"(.*)\" class', str(a))
    #print(title)



    items.append(("https://prisguiden.no" +str(link[0])))


for b in items:
    page = requests.get(b)
    soup = BeautifulSoup(page.content, 'html.parser')


    for a in soup.find_all("h1", class_="product-title"):
        brand = re.findall('product-title\">(.*)<', str(a))



    for a in soup.find_all("div", class_="shop"):

        lager_status = re.findall('<span class=\"quote\">(.*)</span', str(a))
        store = re.findall('<img alt=\"(.*) logo', str(a))
        price = unicodedata.normalize("NFKD",(re.findall(' (.*)</a>', str(a)))[0])
        price = str(price.replace(" ",""))
        if str(lager_status[0]) != "Ikke på lager":
            if str(lager_status[0]) == "På lager":
                lager_status[0] = (bcolors.OKGREEN + lager_status[0] + bcolors.ENDC)
            elif str(lager_status[0]) == "Bekreftet lagerdato":
                lager_status[0] = (bcolors.WARNING + lager_status[0] + bcolors.ENDC)
            elif str(lager_status[0]) == "Kun i butikk":
                lager_status[0] = (bcolors.WARNING + lager_status[0] + bcolors.ENDC)
            elif str(lager_status[0]) == "Forhåndsbestill":
                lager_status[0] = (bcolors.OKCYAN + lager_status[0] + bcolors.ENDC)
            #elif str(lager_status[0]) == "På lager":
            print("Brand: "+brand[0]," | Lager status: "+ lager_status[0], " | Store: " + store[0], " | Pris: " + price+"kr", b)



