websites = (
    "google.com",
    "aitbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tikktok.com"
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)