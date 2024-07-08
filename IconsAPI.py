import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer X0vjEUN6KRlxbp2DoUkyHeM0VOmxY91rA6BbU5j3Xu6wDodwS0McmilLPBWDUcJ1"
}

response = requests.get("https://api.iconfinder.com/v4/iconsets/1761/icons?count=10", headers=headers)

print(response.text)