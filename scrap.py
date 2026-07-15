import requests
import json
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 scrap.py <_intra_42_session_production>")
    sys.exit(1)

session_token = sys.argv[1]

usernames = [
 "oel-feng", "alaassir", "tamounir"
]

cookies = {
    "_intra_42_session_production": session_token
}

folder = "Images"
os.makedirs(folder, exist_ok=True)

for username in usernames:
    url = f"https://profile.intra.42.fr/users/{username}"
    response = requests.get(url, cookies=cookies, allow_redirects=True)

    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            image_url = data['image']['link']
            img_data = requests.get(image_url).content
            path = os.path.join(folder, f"{username}.jpg")
            with open(path, 'wb') as f:
                f.write(img_data)
            print(f"Image for {username} downloaded successfully!")
        except json.JSONDecodeError:
            print(f"[{username}] Response is not valid JSON — probably HTML. Skipping.")
        except KeyError:
            print(f"[{username}] JSON doesn't contain expected image link.")
    else:
        print(f"[{username}] Failed to fetch profile: status code {response.status_code}")
