import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://bank.gov.ua/")
soup = BeautifulSoup(r.text, "lxml")
#task1
#print(soup.find_all("title"))
#task2
#print(soup.find_all("p"))
#task3
#print(len(soup.find_all("p")))
#task4
#print(soup.select("p")[0].get_text())
#task5
#print(len(soup.select("h2")[0].get_text()))
#task6
#print(soup.select("a")[0].get_text())
#task7
#print(soup.select("a")[0]["href"])
#task8
#for li in soup.find_all("li"):
    #print(li.find_next("a")["href"])
#task9
#print(soup.findAll("h2"))
#print(soup.select("h2")[0:4])
#task10
#print(soup.select("a")[0:10])
#task11
#h1 = soup.find_all("h1")
#h2 = soup.find_all("h2")
#h3 = soup.find_all("h3")
#print(list(h1 + h2 + h3))
#task12
#print(soup.select("html")[0].get_text())
#task13
#for i in soup.find_all():
    #print(i.name)task14 
#print(soup.find_all("html"))
#task15
#print(soup.find_all("body"))
#task16
#print(soup.find_all("h1")[1].get_text())
#print(soup.find_all("h1")[1].parent)
#task17
#print(soup.find_all("li"))
#task18
#import re
#for i in soup.find_all(string=re.compile("Python")):
    #print("".join(i.split()))
#task19
#print(soup.find_all(id="top"))
#task20
#print(soup.find_all(href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"))
#task21
#print(soup.select("li > a"))
#task22
#print(soup.find_all(class_="container"))
#task23
#print(soup.find_all("p").remove("py"))
#task24
#print(soup.find_all("p").append("py"))
#task25
#print(soup.find_all("a").insert(0, "Url"))

