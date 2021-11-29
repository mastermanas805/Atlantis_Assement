
"""
task -  Write a python program to scrape a given wikipedia page 
        and return the average of 3 letter, 4 letter and 5 letter
        words per paragraph.
Observation - Wikipedia stores all the paragraphs in div with id = content
"""
import requests
from bs4 import BeautifulSoup
import math

class wiki:
    """
    This is a class that will fetch and compute.
    """
    
    three = []
    four  = []
    five  = []

    def __init__(self):
        data = self.fetchData()
        self.data = self.filterData(data)
        self.output()
    
    def output(self):
        print(f"Output: 3-letter words: {math.floor(sum(self.three)/len(self.three))}/paragraph. 4-letter words: {math.floor(sum(self.four)/len(self.four))}/paragraph. 5-letter words: {math.floor(sum(self.five)/len(self.five))}/paragraph")
    
    
    @staticmethod
    def fetchData():
        link = input("Enter wikipedia page? ")
        try:
            page = requests.get(link)
        except:
            Exception("Enter Valid Link")
        return page.text
    
    @staticmethod
    def processpara(text):
        text = text.split(" ")
        res = [0,0,0]
        for i in text:
            if len(i) == 3:
                res[0]+=1
            elif len(i) == 4:
                res[1]+=1
            elif len(i) == 5:
                res[2]+=1
        return res

    def filterData(self, html):
        soup = BeautifulSoup(html, features='html.parser')
        soup = soup.findAll('div', {'id': 'content'})
        ret = {}
        th,fo,fi = 0,0,0
        #map links and texts
        for i in soup:
            for j in i.find_all('p'):
                t = j.get_text()
                if len(t)>0 and t != "\n" and t != " ":
                    a,b,c = self.processpara(t)
        
                    self.three+=[a]
                    self.four+=[b]
                    self.five+=[c]

def main() -> None:
    w = wiki()
  
if __name__=="__main__":
    main()