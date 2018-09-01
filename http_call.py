import requests
for i in range(3):
    req = requests.get('https://webhook.site/6b8e6e34-21c6-4b6f-afbe-8398b4502003')
    print(req.headers['Date'])