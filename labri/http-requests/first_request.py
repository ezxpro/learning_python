import requests

# full documentation can be found here: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request

# getting a webpage
response = requests.get("https://api.github.com/events")

''' other HTTP methods include
    PUT = requests.put()
    DELETE = requests.delete()
    HEAD = requests.head()
    OPTIONS = requests.options()
'''

''' Passing parameters in URLs
    To pass data in the format http://somesite.com/get?key=val
    Pass a 'params' argument the method in question, where
    'params' is a python dictionare, whose keys and values will
    respectively be the 'key' and 'val' in the URL, like in the
    example above
'''
