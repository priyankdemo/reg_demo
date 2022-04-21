# mportin the requestsli brary
import requests

# defining the api-endpoint
API_ENDPOINT = "http://8ede-111-93-95-94.ngrok.io/train"

# data to be sent to api
data = {
	"url": "https://github.com/priyankdemo/reg_demo_tw1",
	"branch_name": "master",
	"user_name": "demo@mlops.com"
}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is :%s"%pastebin_url)
