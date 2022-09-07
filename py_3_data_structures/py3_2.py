from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
    "https://httpstat.us/502",
    "https://httpstat.us/404",
    "https://httpstat.us/300",
    "https://httpstat.us/101"
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code >= 500:
        results[website] = "server error"
    elif response.status_code >= 400:
        results[website] = "client error"
    elif response.status_code >= 300:
        results[website] = "redirection"
    elif response.status_code >= 200:
        results[website] = "successful"
    else:
        results[website] = "information"

print(results)