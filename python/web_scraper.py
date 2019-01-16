import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "https://www.google.com/search?q="
print("Enter keyword to search!")
s = input()
URL += s
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
  
results=[]

for row in soup.findAll(class_='g'):
    r = row.find(class_='r')
    s = row.find(class_='st')
    result = {}
    result['heading'] = r.a.text 
    result['url'] = r.a['href'] 
    result['description'] = s.text
    results.append(result) 
  
filename = 'results.csv'
with open(filename, 'wb') as f:
    f = open("results.csv", 'w',newline = "")
    w = csv.DictWriter(f,['heading','url','description'])
    w.writeheader()
    for quote in results:
        print(quote)
        w.writerow(quote)
