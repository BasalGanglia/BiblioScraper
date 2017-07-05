import requests
from fake_useragent import UserAgent
#
# url = 'http://codingbat.com/java'
# file_name = 'codingbat_exercises.txt'
#
# user_agent = UserAgent()
# page = requests.get(url, headers ={'user-agent':user_agent.chrome})
#
# with open(file_name,'w') as file:
#     file.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)

from bs4 import BeautifulSoup
#
# def read_file():
#     file = open('codingbat_exercises.txt')
#     data = file.read()
#     file.close()
#     return data
#
# soup = BeautifulSoup(read_file(), 'lxml')
#
# all_divs = soup.find_all('div', attrs={'class':'summ'})

user_agent = UserAgent()
main_url = 'http://codingbat.com/java'

page = requests.get(main_url, headers={'user-agent':user_agent.chrome})
soup = BeautifulSoup(page.content, 'lxml')

base_url = 'http://codingbat.com'

all_divs = soup.find_all('div', class_ ='summ')

all_links = [base_url + div.a['href'] for div in all_divs]


for link in all_links:
    inner_page = requests.get(link,headers={'user-agent':user_agent.chrome})
    inner_soup = BeautifulSoup(inner_page.content, 'lxml')
    div = inner_soup.find('div', class_='tabc')
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]
    # for question_link in question_links:
    #     print(question_link)
    # break

    for question_link in question_links:
        final_page = requests.get(question_link)
        final_soup = BeautifulSoup(final_page.content, 'lxml')
        indent_div = final_soup.find('div', attrs={'class':'indent'})
        problem_statement = indent_div.table.div.string

        siblings_of_statement = indent_div.table.div.next_siblings

        examples = [sibling for sibling in siblings_of_statement if sibling.string is not None]

        for example in examples:
            print(example)
        #for sibling in siblings_of_statement:
        break
    break