import requests

ct = 1
while True:
    
    res = requests.get("http://34.107.198.190/")
    print(f"Ping {ct} {res.status_code}")
    
    ct += 1
