from api.sendMessage import send_message

name = 'hello'
description = 'A simple greeting command.'
admin_bot = False

def execute(sender_id, message_text):
    response_message = {"text": f"Hello! How can I assist you?"}
    send_message(sender_id, response_message)
