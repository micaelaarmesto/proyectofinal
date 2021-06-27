import requests
url = "https://itunes.apple.com/search?parameterkeyvalue"
key1 = value1
args = {"term" : jack+johnson}
response = requests.get(url, params=args)
cant.Canciones = response.json()["total.Results"]
print("Cantidad de canciones: ", cantCanciones)