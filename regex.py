import re


nameRegex = re.compile(r'zhex')
mo = nameRegex.search('My name is zhexiong wei, also zhex in my company')
print mo.group()
