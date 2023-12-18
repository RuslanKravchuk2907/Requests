import requests
from API import API_TOKEN

data = {"custname": "Руслан Кравчук",
"custtel": "601591",
"custemail": "lan164@gmail.com",
"size": "small",
"topping": "bacon",
"topping": "onion",
"delivery":"",
"comments":"",  }

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,uk;q=0.6",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6580b131-1a58a7867eb75c1b5eb114b7"
  }

variable = requests.Session()

var = variable.get("https://httpbin.org/form/post")

#response = requests.get("https://httpbin.org/headers", headers=headers)

response = variable.post("https://httpbin.org/post", headers=headers, data=data)


print(response.status_code)
# print(response.headers)
# print(response.text)
print(response.json())