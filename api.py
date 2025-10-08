import requests

url = "https://api.languagetool.org/v2/check"
data = {
    "text": "He go to school every day.",
    "language": "en-US"
}

response = requests.post(url, data=data)
result = response.json()

print(result)
