#-*- coding: UTF-8 -*-


from bs4 import BeautifulSoup
with open("ecologicalpyramid.html","r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid,"html.parser")
    producer_entries = soup.find("ul")
    print(producer_entries.li.div.string)
