# IPython log file

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)
res.status_code == requests.codes.ok
len(res.txt)
len(res.text)
print(res.text[:250])
print res.text[:250]
print(u' res.text[:250])
data = {i:randn() for i in range(7)}
from numpy.random import randn
data = {i:randn() for i in range(7)}
print data
an_apple = 27
an_example = 42
an_example
b = [1,2,3]
b.reverse()
b
get_ipython().magic(u'pinfo b')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd my-practice-git/')
get_ipython().magic(u'run mapIt.py')
get_ipython().magic(u'paste')
get_ipython().magic(u'logstart')
get_ipython().system(u'python')
ip_info = get_ipython().getoutput(u'ifconfig eth0 | grep "inet "')
ip_info[0].strip()
get_ipython().magic(u'ls ')
get_ipython().system(u'ls')
exit()
