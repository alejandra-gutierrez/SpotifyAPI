import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import tabulate

url = "https://www.thewrap.com/all-52-game-of-thrones-main-characters-ranked-coronavirus-quarantine/"

# Extract the content
r = requests.get(url)
c = r.content

# Create a soup object
soup = BeautifulSoup(c, features="html.parser")
soup.get_text(separator="\n")
# print(soup.prettify())

main_content = soup.findAll('strong')
# print(main_content)
listToStr = ""
nameList = [i.text for i in main_content]
listToStr = ' '.join([str(elem) for elem in nameList])
listToStr = re.sub(r'\([^()]*\)', ',', listToStr)
df = pd.Series(nameList)
df = df.to_frame()
df.columns = ["column1"]

print(df.info())
new= df["column1"].str.split(".", n = 1, expand = True)

# making separate last name column from new data frame
df["name"] = new[1]


df.drop(['column1'], axis=1, inplace = True)
print(df)
df.to_csv('GoT_characters.csv')
# text_file = open("test.txt", "w")
# n = text_file.write(df)
#
# read_file = pd.read_csv(r'test.txt', header = None,  error_bad_lines=False)
# read_file.to_csv(r'GoT_characters.csv', index=None)

# Extract the relevant information as text

# content1 = main_content.findAll('li')
# # print(type(content1))
# nameList = [i.text for i in content1]
# print(nameList)
# listToStr = ' '.join([str(elem) for elem in nameList])
#
# listToStr = re.sub(r'\([^()]*\)', ',', listToStr)
# print(listToStr)
# S = pd.Series(nameList)
# S.to_frame()
# print(S.head())
# print(S.shape)
#
# name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)')
#
# names = name_pattern.findall(content)
# print(names)

