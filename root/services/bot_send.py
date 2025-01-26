import requests
from datetime import datetime
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
def send_msg(**kwargs):
    token = "your bot token"  # bot token

    user_id = "your telegram id"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {kwargs} </b> ')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())

