import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("http://books.toscrape.com/")
r.content

# Use the 'html.parser' to parse the page content and store it in a variable.
soup = BeautifulSoup(r.content, 'html.parser')

# Find all the book titles on the webpage
for book in soup.find_all('h3'):
    print(book.get('title'))