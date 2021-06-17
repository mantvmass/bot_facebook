from flask import Flask, request
from pymessenger.bot import Bot
import time
from weather import key1, key2, key3, key4, key5, key6, key7, key8, key9, key10, key11, key12, welcome



app = Flask(__name__)

ACCESS_TOKEN = "your token"
VERIFY_TOKEN = "hellobot"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def bot_messenger():
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
                    
                    recipient_id = data['recipient']['id']
                    recipient_id = data['sender']['id']
                    #sender_id = data['sender']['id']
                    #sender_id = data['recipient']['id']

                    if data['message'].get('text'):
                        msg = data['message']['text']
                        print(f"ข้อความที่ได้รับคือ ---- {msg}")

                        if msg == key1 or msg == key2 or msg == key3 or msg == key4 or msg == key5 or msg == key6 or msg == key7 or msg == key8 or msg == key9 or msg == key10 or msg == key11 or msg == key12:                            
                            bot.send_text_message(recipient_id, welcome)
                            bot.send_text_message(recipient_id, timer())
                            #bot.send_text_message(sender_id, welcome)
                            #bot.send_text_message(sender_id, timer())

                        else:
                            pass

                else:
                    pass
        return "ok"

def timer():
    timeis = time.localtime()
    tt = time.strftime('%A %d %B %Y, %H:%M:%S', timeis)
    return tt



if __name__ == "__main__":
    app.run(port=5002, debug=True)