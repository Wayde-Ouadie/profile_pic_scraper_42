import requests
import json

usernames = [
 "ahari","mamal","nrais","ahmima","azahid","irabhi","nlotfi","otouba","safifi","sasbai","souali","yrafai","aanbadi","amahdad",
 "arahhab","arokhsi","bkolani","mofouzi","sel-mir","ybennis","yhajjar","ylabser","aait-laf","aait-oui","abahadda","absabbar","aces-sal",
 "achnouri","aelkhadr","aguenzao","alkhbiri","asadkaou","ayelaraf","ctoujana","doaghmir","imsbaiti","kabouelf","khabdelf","lhchiban","maboulah","mbeniour","mboulagh","mel-moud","mohel-bo",
 "nbougrin","rboukhra","rsaadani","wabourah","wel-bagh","yabounna","zaafrani","zyahansa","akaabi","isidki","snjili","ynachat",
 "zchbani","abkacimi","eoussama","hmokhtar","kaafkhar","lbenhamd","meserghi","mhaddaou","ouaarabe","rbouizer","rgatnaou","soel-bou","tboussad","wzrhaida"
]

cookies = {
    "_intra_42_session_production": "88cd80ed5dfba950f9fea493f332f0c6" # 7AT HNA _intra_42_session_production jibo mn l cookies dl intra
}

for username in usernames:
    url = f"https://profile.intra.42.fr/users/{username}"

    response = requests.get(url, cookies=cookies, allow_redirects=True)

    if response.status_code == 200:
        data = json.loads(response.text)

        image_url = data['image']['link']

        img_data = requests.get(image_url).content

        with open(f"{username}.jpg", 'wb') as f:
            f.write(img_data)

        print(f"Image for {username} downloaded successfully!")
    else:
        print(f"Failed to fetch data for {username}")

