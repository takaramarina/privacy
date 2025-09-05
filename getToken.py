import requests

url = "https://graph.facebook.com/v20.0/oauth/access_token"
params = {
    "grant_type": "fb_exchange_token",
    "client_id": "YOUR_APP_ID",
    "client_secret": "YOUR_APP_SECRET",
    "fb_exchange_token": "YOUR_SHORT_LIVED_TOKEN"
}

response = requests.get(url, params=params)
print(response.json())
