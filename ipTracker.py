import requests
from bs4 import BeautifulSoup
import sys

ip = sys.argv[1]
url = (f"https://www.shodan.io/search?query={sys.argv[1]}")

headers = {
    "Cookie": 'polito="fdb411d9a44cbeb849b3c75d8a4c046f66ad6e0066ad665bb60c4284d9dbb43f!"',
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Accept-Language": "pt-BR",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.shodan.io/host/138.207",
    "Accept-Encoding": "gzip, deflate, br"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
#Adicionar mais sites para busca reversa
