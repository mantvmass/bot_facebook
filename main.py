from flask import Flask, request
from pymessenger.bot import Bot
import time
from weather import *


app = Flask(__name__)

ACCESS_TOKEN = "your token"
VERIFY_TOKEN = "set verify token"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def bot_messenger(): # Function เช็ค Verify Token
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
     
        for event in output['entry']:
            message = event['messaging']
            for data in message:
                if data.get('message'):
                    
                    recipient_id = data['recipient']['id'] # รับข้อความจากแอดมินเพจ
                    u_recipient_id = data['sender']['id']  # รับข้อความจากลูกค้า

                    if data['message'].get('text'):
                        msg = data['message']['text']
                        print(f"\033[42mmessage\033[0m: \033[32m{msg}\033[0m")

                        if msg == key1 or msg == key2 or msg == key3 or msg == key4 or msg == key5 or msg == key6 or msg == key7 or msg == key8 or msg == key9 or msg == key10 or msg == key11 or msg == key12 or msg == key13:                            
                            bot.send_text_message(recipient_id, welcome)
                            bot.send_text_message(recipient_id, timer())
                            bot.send_text_message(u_recipient_id, timer())
                        else:
                            pass

                        if msg == "DEV":
                            bot.send_text_message(recipient_id, dev)
                            bot.send_text_message(u_recipient_id, dev)
                        else:
                            pass
                else:
                    pass
        return "ok"

def timer(): # Function บอกเวลา
    timeis = time.localtime()
    tt = time.strftime('%A %d %B %Y, %H:%M:%S', timeis)
    return tt



if __name__ == "__main__":
    app.run(port=9080, debug=True)
