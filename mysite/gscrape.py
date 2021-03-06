import requests
import bs4

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text = "nursing home"
query_root = "https://news.google.co.in/"
# 'https://google.com/search?q='

url = query_root + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result = requests.get(url)

# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,
                         "html.parser")
# print(soup)
heading_object = soup.find_all('h3')
headings_list = []

for info in heading_object:
    print(info.getText())
    headings_list.append(info.getText())
