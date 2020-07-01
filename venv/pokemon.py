import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import tabulate


url = "https://www.pokemon.com/us/pokedex/"

# Extract the content
r = requests.get(url)
c = r.content

# Create a soup object
soup = BeautifulSoup(r.text, "html.parser")

main_content = soup.find('div', {'class': 'container pokedex'})
print(main_content)
results = soup.find('ul', {'class': 'results'})
# print(results)
# links = results.find("li")
#
# for item in links:
#     item_text = item.find("a").text
#     item_href = item.find("a").attrs["href"]
#     print(item_text)
#     print(item_href)
