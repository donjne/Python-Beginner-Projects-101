#textbelt is a library that is going to handle sending of the messages
#schedule is the library that is going to handle when we want this message or scripts to be executed

import requests
import schedule
import time

def send_message():
    resp = requests.post(('https://textbelt.com/text'), {
        'phone': '+2348025950834',
        'message': 'Good morning boss. Your daily hot tea is ready at the office.',
        'key': 'textbelt'
    })
    print(resp.json())

    # schedule.every().day.at('9:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)