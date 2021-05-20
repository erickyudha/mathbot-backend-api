import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import arithmetic
import factorial
import modulo
import sum_combination
import sum_permutation


def send(event, text):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text)
    )

user_position = {}

user_var_storage = {}

app = Flask(__name__)

line_bot_api = LineBotApi('')
handler = WebhookHandler('')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Here's all the messages will be handled and processed by the program """

    msg = (event.message.text).lower().lstrip()
    profile = line_bot_api.get_profile(event.source.user_id)
    try:
        user_position[f'{profile.user_id}']
    except:
        user_position[f'{profile.user_id}'] = 0

    if msg == '-menu':
        user_position[f'{profile.user_id}'] = 0

    elif user_position[f'{profile.user_id}'] == 0:
        if msg == '-calculator':
            send(event, arithmetic.MENU_TEXT)
            user_position[f'{profile.user_id}'] = 1
        elif msg == '-factorial':
            send(event, factorial.MENU_TEXT)
            user_position[f'{profile.user_id}'] = 2
        elif msg == '-modulo':
            send(event, modulo.MENU_TEXT)
            user_position[f'{profile.user_id}'] = 3
        elif msg == '-permutation':
            send(event, sum_permutation.MENU_TEXT)
            user_position[f'{profile.user_id}'] = 4
        elif msg == '-combination':
            send(event, sum_combination.MENU_TEXT)
            user_position[f'{profile.user_id}'] = 5
        else:
            send(event, 'Try Again! -menu to go back to main menu')

    elif user_position[f'{profile.user_id}'] == 1:
        if msg == '-exit':
            send(event, 'Thanks for using arithmetic calculator by MathBot!')
            user_position[f'{profile.user_id}'] = 0
        else:
            send(event, arithmetic.main_calc(profile.user_id, msg))

    elif user_position[f'{profile.user_id}'] == 2:
        if msg == '-exit':
            send(event, 'Thanks for using factorial calculator by MathBot!')
            user_position[f'{profile.user_id}'] = 0
        else:
            send(event, factorial.factorial(msg))
            
    elif user_position[f'{profile.user_id}'] == 3:
        if msg == '-exit':
            send(event, 'Thanks for using modulo calculator by MathBot!')
            user_position[f'{profile.user_id}'] = 0
        else:
            send(event, modulo.modulo(msg))

    elif user_position[f'{profile.user_id}'] == 4:
        if msg == '-exit':
            send(event, 'Thanks for using permutation calculator by MathBot!')
            user_position[f'{profile.user_id}'] = 0
        else:
            send(event, sum_permutation.main(msg))

    elif user_position[f'{profile.user_id}'] == 5:
        if msg == '-exit':
            send(event, 'Thanks for using combination calculator by MathBot!')
            user_position[f'{profile.user_id}'] = 0
        else:
            send(event, sum_combination.main(msg))





if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
