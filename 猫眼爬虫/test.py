import requests

url = "https://maoyan.com/board/4?offset=0"
headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}
response = requests.get(url, headers=headers)
# return response.text
print(response.text)