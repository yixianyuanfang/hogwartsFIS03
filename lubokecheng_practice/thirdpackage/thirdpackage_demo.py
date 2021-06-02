import requests

# r = requests.get("http://www.baidu.com")

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r.text)
