import requests
import json
import sys

if (len(sys.argv) < 2:
   print("Usage: python3 scrap.py <_intra_42_session_production>")
	sys.exit(1)

session_token = sys.argv[1]

usernames = [
 "ahari","mamal","nrais","ahmima","azahid","irabhi","nlotfi","otouba","safifi","sasbai","souali","yrafai","aanbadi","amahdad",
 "arahhab","arokhsi","bkolani","mofouzi","sel-mir","ybennis","yhajjar","ylabser","aait-laf","aait-oui","abahadda","absabbar","aces-sal",
 "achnouri","aelkhadr","aguenzao","alkhbiri","asadkaou","ayelaraf","ctoujana","doaghmir","imsbaiti","kabouelf","khabdelf","lhchiban","maboulah","mbeniour","mboulagh","mel-moud","mohel-bo",
 "nbougrin","rboukhra","rsaadani","wabourah","wel-bagh","yabounna","zaafrani","zyahansa","akaabi","isidki","snjili","ynachat",
 "zchbani","abkacimi","eoussama","hmokhtar","kaafkhar","lbenhamd","meserghi","mhaddaou","ouaarabe","rbouizer","rgatnaou","soel-bou","tboussad","wzrhaida"
]

cookies = {
	"_intra_42_session_production": session_token
}

for username in usernames:
	url = f"https://profile.intra.42.fr/users/{username}"
	response = requests.get(url, cookies=cookies, allow_redirects=True)

	if response.status_code == 200:
		try:
			data = json.loads(response.text)
			image_url = data['image']['link']
			img_data = requests.get(image_url).content
			with open(f"{username}.jpg", 'wb') as f:
				f.write(img_data)
			print(f"Image for {username} downloaded successfully!")
		except json.JSONDecodeError:
			print(f"[{username}] Response is not valid JSON — probably HTML. Skipping.")
		except KeyError:
			print(f"[{username}] JSON doesn't contain expected image link.")
	else:
		print(f"[{username}] Failed to fetch profile: status code {response.status_code")}
