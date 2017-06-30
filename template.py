# -*- coding: utf-8 -*-
"""

Python refresher

Created on %(date)s

@author: Ilkka Kosunen
"""

####### Lists

my_list= [4,3,2,1]
print(my_list[0])

my_list.append(5)
my_list.pop()
my_list

my_list.insert(1,100)
my_list

##### Dictionaries


my_dict = {}
my_dict

my_dict = {'school': 'definition of school', 'coding':'defintion of coding', 'python':'defintion of python'}
my_dict['school']

my_dict['pen'] = 'def of pen'
my_dict

for key,value in my_dict.items():
    print(key, ' ', value)

my_dict[2] = ' the key is 2 '
my_dict

### Tuples

person = 'Samy', 27,'brown'   # Boxing
name,age,hair_color = person   # unboxing

for value in person:
    print(value)

# nested tuple

person2 = 'Samy', ('brown','black'), 27
person2[1]

## Remember, tuple is immutable

# List Comprehension
import random

our_list = []
for value in range(0,20):
    our_list.append(random.randint(0,100))

## our_list 20 random nums now

## List comprehension : [value which is being inserted into my list -- for loop
new_list = [value for value in range(0,20)]
new_list3 = [random.randint(0,100) for value in range(0,20)]

carts= [['toothpaste','shoes','bread'],['pencils','erasers','notebook'],['meat','fruit','vegetables']]

person1 = ['toothpaste','shoes','bread']
person2 = ['pencils','erasers','notebook']
person3 = ['meat','fruit','vegetables']

carts2 = [person1,person2,person3]
carts == carts2

for value in carts:
    print(value)

task_list = []
for row in range(0,25,5):
    inner_list = []
    for column in range(row, row+5):
        inner_list.append(column)
    task_list.append(inner_list)

# Use list comprehension to make the 2-d list

new_list = [[column for column in range(row,row+5)]for row in range(0,25,5)]

### inline if else

a= 20
if a == 20:
    print('a is 20')
else:
    print('a is not 20')

print('a is 20' if a == 21 else 'a is not 20')

b = True if a == 20 else False
b

num = [value for value in range(-5,5)]
print(num)

positive_num = [value for value in num if value < 0]
positive_num


## EXCEL READING WRITING
from xlsxwriter import Workbook

#Make a workbook
workbook = Workbook('first_file.xlsx')

worksheet = workbook.add_worksheet()

# Write function

worksheet.write(0,0,'zero, row and zero column')
worksheet.write(0,1,'zero row one column')
worksheet.write(1,0,'one, row and zero column')
worksheet.write(1,1,'one row one column')



workbook.close()

## REAding
workbook = xlrd.open_workbook('first_file.xlsx')

worksheet = workbook.sheet_by_index(0)

rows = worksheet.nrows

for row in range(rows):
    first_col, second_col = worksheet.row_values(row)
    print(first_col, ' ', second_col)

workbook.close()

#### Soup example

from bs4 import BeautifulSoup
import requests

url = "http://example.com/"

# Getting the webpage, creating a Response object.
response = requests.get(url)

#Extracting the source code of the page
data = response.text

#Passing the source to soup
soup = BeautifulSoup(data, 'html.parser')

#Extracting all the <a> tags into a list
tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))



####################


response = requests.get('https://www.google.com')

print(response.content)


########### READ EXAMPLE.html

import lxml

def read_file():
    file = open('example.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'html.parser')
print(soup.prettify())

soup.body['style'] = 'puppe'














