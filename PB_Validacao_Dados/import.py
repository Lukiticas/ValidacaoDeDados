import requests, json

r = requests.get("https://viacep.com.br/ws/83085100/json/")
rs = r.text
rj = json.loads(rs )
print(rj["bairro"])