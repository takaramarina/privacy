import requests

url = "https://graph.facebook.com/v20.0/oauth/access_token"
params = {
    "grant_type": "fb_exchange_token",
    "client_id": "1279833370025992",
    "client_secret": "7c3dced26218afc9582ccfb7053a2e03",
    "fb_exchange_token": "EAASMAG1kYAgBPfvhVvkK1vHMgHKKB7If3MZCsfMpjUrDIdEZAFcGxULrmoPwUR0dVMDzi09JD1wFHzZB9dxQe3O8Q04eBkAZA9IaUAqTHKqQNKeU7fnatAGrq0CwAdhqJ9ZAoVbIDXozNivFoGBW7jj2qJ7ZCKZASxj267NJ7JkMFxZBr5RZBRoxqX0a52XGcpvMYZCspgvrITZCySsb7SGqpTLiYitSQOiczGASlUZByhgQLxxLhqzo316E"
}

response = requests.get(url, params=params)
print(response.json())
