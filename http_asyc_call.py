import grequests
urls = ['https://webhook.site/6b8e6e34-21c6-4b6f-afbe-8398b4502003'] * 3
request = (grequests.get(url) for url in urls)
responses = grequests.map(request)
for response in responses:
    print(response.headers['Date'])
