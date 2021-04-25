from GoogleNews import GoogleNews
googlenews = GoogleNews()

googlenews = GoogleNews(lang='en')
googlenews = GoogleNews(period='7d')
googlenews = GoogleNews(encode='utf-8')
googlenews = GoogleNews(start='02/01/2019', end='02/28/2020')

# googlenews.set_lang('en')
# googlenews.set_period('7d')
# googlenews.set_encode('utf-8')


#googlenews.set_time_range('02/01/2020', '02/28/2020')

'''
googlenews.search('emeritus senior living')
# googlenews.get_news('APPLE')


# print(type(googlenews.get_texts()))

title_list = googlenews.get_texts()

diction = googlenews.results()
for item in diction:
    print(item)
    print("\n")
    print(item.keys())
    print("\n")
    print(item['desc'])
    print("\n\n")

# for item in title_list:
#    print(item + "\n")
'''


def get_title_text(search_string):
    googlenews.search(search_string)
    title_list = googlenews.get_texts()
    return title_list


#gets json of results
def get_results(search_string):
    googlenews.search(search_string)
    diction = googlenews.result()
    return diction
