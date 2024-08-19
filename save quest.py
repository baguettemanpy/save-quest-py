
import requests


print("hi")


accid = ""

# URL d'authentification et données
auth_url = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token"
auth_form_data = {
    "grant_type": "device_auth",
    "device_id": "",
    "account_id": accid,
    "secret": ""
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='
}

auth_response = requests.post(auth_url, headers=headers, data=auth_form_data)
if auth_response.status_code == 200:
    access_token = auth_response.json().get("access_token")
    if not access_token:
        print("Failed to retrieve access token")
    else:


        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accid}/client/ClientQuestLogin?profileId=campaign&rvn=-1"

        payload = {}

    
    
        response = requests.post(url, headers=headers, json=payload)  
        response.raise_for_status()  
        

        if response.status_code == 200:
            print("SAVE QUEST DONE")
        else:
            print("error")
else:
    print(f"Authentication error: {auth_response.status_code}")
