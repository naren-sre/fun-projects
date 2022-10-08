import requests

response =requests.get("https://api.instrumental.ai/healthcheck",timeout=5)
print(response.status_code)


