from bs4 import BeautifulSoup
import re

def read_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#print(soup.find_all('b'))
#
# # tag names that start with b
# regex = re.compile('^b')
#
# for tag in soup.find_all(regex):
#     print(tag.name)
#
# # Print all tags that contain t
# regex = re.compile('t')
# for tag in soup.find_all(regex):
#     print(tag.name)

# find can take lists: all a and b tags:

# for tag in soup.find_all(['a','b']):
#     print(tag.name)

# usinga  function

# def has_class(tag):
#     return tag.has_attr('class')
#
# for tag in soup.find_all(has_class):
#     print(tag.name)
#


## FIND_ALL
## Signature: find_all(name, attrs, recursive, string, limit, **kwargs)
#
# a_tags = soup.find_all('a')
# for a in a_tags:
#     print(a)
#
# attr ={'class':'sister', 'id':'link1'}
# first_a = soup.find_all('a', attrs= attr)
# print(first_a)
#
# attr ={'class':'sister'}
# first_a = soup.find_all('a', attrs= attr)
# print(first_a)

# Limit parameter
#
# a_tags = soup.find_all('a', limit=1)
# print(a_tags)

## String parameter
#
# regex = re.compile('Elsie')
#
# tag = soup.find_all(string=regex)
# print(tag)

## **kwargs argument:
#
# tags =soup.find_all(class_  ='sister')
# for tag in tags:
#     print(tag)

## Recursive
#
# title = soup.find_all('title') #, recursive = False)
#
# print(title)


## The Find function
## Signature : find(name,attrs, recursive, string, **kwargs)
# returns a single object if found -- in case of multiple objects, it returns the first