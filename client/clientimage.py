import requests

resp = requests.post("https://olahcitra-api.herokuapp.com/predict", files={"file": open('/client/wallbg.jpg', 'rb')})

print(resp.json())
