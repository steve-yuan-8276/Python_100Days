import urllib.request

url = "http://helloworldbook2.com/data/message.txt"
with urllib.request.urlopen(url) as response:
    message = response.read().decode("utf-8")

print(message)