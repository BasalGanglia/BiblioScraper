from bs4 import BeautifulSoup

def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

all_divs = soup.find_all('div', attrs={'class':'entry-letter'})

# for div in all_divs:
#     print(div.div.a.span.string)

products = [div.div.a.span.string for div in all_divs]

products = {}  # Key anme, link  -value

product_names = [div.div.a.span.string for div in soup.find_all('div', class_='entry-letter')]

product_links = [div.div.a['href'] for div in soup.find_all('div', class_='entry-letter')]
# product_links[2]
# products[2]

products = {div.div.a.span.string:div.div.a['href'] for div in soup.find_all('div', class_ = 'entry-letter')}