import requests
import time
from bs4 import BeautifulSoup


url = "https://www.imdb.com/list/ls047915915/"

response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


list_items = soup.find_all("div", class_="lister-item-content")


for item in list_items:
    # Title
    title = item.find("a").text.strip()
   
    
    # Year
    year = item.find("span", class_="lister-item-year").text.strip()
    
    # Rating
    rating = item.find("span", class_="ipl-rating-star__rating").text.strip()
    
    # Description
    description = item.find("p", class_="").text.strip() if item.find("p", class_="") else "Description not available"
    time.sleep(1)
    
    print("Title:-", title)
    print("Year:-", year)
    print("Rating:-", rating)
    print("Description:", description)
    print()
