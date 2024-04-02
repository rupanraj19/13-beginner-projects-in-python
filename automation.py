# import requests 
# import schedule
# import time
# Textbelt.com  (http://www.textbelt.com) api to send text messages

import time
import requests
import schedule

def send_sms():
    resp = requests.post('https://textbelt.com/text',{
        'phone' : 'xxxxxxxx', # phone number with country code
        'message' : "Hello",
        'key': 'textbelt'
    })

    print(resp.json())

# schedule.every().day.at('19:35').do(send_message)
send_sms()