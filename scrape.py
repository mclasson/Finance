import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
import untangle
import xmltodict

# Hämta hela webbsidan
html_text = requests.get("https://fi.se/sv/vara-register/fondinnehav-per-kvartal/").text
soup = BeautifulSoup(html_text, 'html.parser')


for link in soup.find_all('a'): # Leta upp alla länkar
    href = link.get('href') # Hämta deras href
    if(href.startswith("/sv/vara-register/fondinnehav-per-kvartal/download/")): #Kolla så att det är en länk med zip
        r = requests.get("https://fi.se/" + href) # Hämta den zippen
        filename=href.split('=')[1] # Kolla vad de kallar filen
        with open(filename, 'wb') as f:
            f.write(r.content)
    
for file in os.listdir():
    if(file.endswith("zip")):
        with ZipFile(file, 'r') as zipObject:
            zipObject.extractall("data")

for dir in os.listdir("data"):
    for file in os.listdir("data/"+dir):
        if(file.endswith("xml")):
            with open("data/" + dir + "/" + file,'r',encoding='utf8') as fd:
                doc = xmltodict.parse(fd.read())
                bolag = doc["VärdepappersfondInnehav"]["Bolagsinformation"]["Fondbolag_namn"]
                print(bolag)
                alla_fin_instr = doc["VärdepappersfondInnehav"]["Fondinformation"]



