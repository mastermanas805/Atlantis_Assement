"""
Task 

Write a python program to scrape the list of links available in this Github repository (https://github.com/vinta/awesome-python) and search them by exact name from the console. 
Search result should return the github url of the result repository. 

Observation

All the links are present in readme.md of the file

Approach
    1. Make a request to get the readme.md file content at https://raw.githubusercontent.com/vinta/awesome-python/master/README.md
    2. Convert MD to the HTML
    3. Extract the links with BeautifulSoup package in python
    4. Store the data in a dictionary with format {"alt_text":"link"}
"""
import requests
import markdown
from bs4 import BeautifulSoup

class linkQuery:
    """
    This is a class that will fetch and store the links. It will also provide
    an query interface for the links
    """
    def __init__(self):
        data = self.fetchData()
        self.data = self.filterData(data)
    
    def query(self):
        i = input("Query? ")
        print("Output: ", self.data.get(i, "Invalid Input"))
    
    @staticmethod
    def fetchData():
        # Get the raw md data
        md = requests.get('https://raw.githubusercontent.com/vinta/awesome-python/master/README.md')
        # md = requests.get("https://github.com/vinta/awesome-python")
        # Convert md to html
        html = markdown.markdown(md.text)
        return html
    
    @staticmethod
    def filterData(html):
        soup = BeautifulSoup(html, features='lxml')
        ret = {}
        #map links and texts
        for i in soup.find_all('a'):
            if i.get_text():
                ret[i.get_text()] = i.get('href')
        return ret
        
def main():
    lq = linkQuery()
    lq.query()
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()