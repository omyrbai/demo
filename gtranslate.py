import requests

url = "https://translate.google.com/?sl=en&tl=kk&text=need&op=translate"
resp = requests.get(url)

print(resp.text)
