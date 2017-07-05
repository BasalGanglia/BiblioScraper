import re

regex = re.compile('[1-4]')
print(regex.match('3'))
print(regex.match('7'))

# Complement
regex = re.compile('[^a-zA-Z]')

print(regex.match('d'))

# Matc hany decimal digit

regex = re.compile('\d')

