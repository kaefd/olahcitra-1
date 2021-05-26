import requests

resp = requests.post("https://olahcitra-1.herokuapp.com/predict", files={"file": open('wallbg.jpg', 'rb')})

print(resp.json())
