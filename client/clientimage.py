import requests

resp = requests.post("https://olahcitra-1.herokuapp.com/predict", files={"file": open('/client/wallbg.jpg', 'rb')})

print(resp.json())
