from tranco import Tranco
import json

# Initialize Tranco list
tr = Tranco(cache=True)
top = tr.list().top(1_000_000)  # or 1_000_000 for full list

# Create dictionary with key as site name (no .com/.net) and value as full URL
website_dict = {}

for domain in top:
    site_name = domain.split('.')[0]  # Remove .com/.net/etc
    if site_name not in website_dict:  # Avoid duplicates
        website_dict[site_name] = f"https://{domain}"

# Save to JSON
with open("cleaned_websites.json", "w", encoding="utf-8") as f:
    json.dump(website_dict, f, indent=2)

print("✅ Cleaned dataset saved as cleaned_websites.json")
