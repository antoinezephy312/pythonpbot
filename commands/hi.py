from api.sendMessage import send_message

name = 'hi'
description = 'A greeting command to say hi to the user.'
admin_bot = False

def execute(sender_id, message_text):
    if message_text.strip().lower() == name:
        response_message = {"text": f"Hello! You used the {name} command."}
        send_message(sender_id, response_message)
