import requests
from api.sendMessage import send_message

name = 'ai'
description = 'An AI-powered greeting command using GPT-4o.'
admin_bot = False

# Define the API URL
api_url = "https://joshweb.click/api/gpt-4o"


def execute(sender_id, message_text):
    # Prepare the query for the AI model
    params = {
        'q': message_text,  # The user's message text to query
        'uid': sender_id  # Unique identifier for the user
    }

    try:
        # Make a request to the API
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Extract the response text from the API
        data = response.json()
        ai_response = data.get("response", "Sorry, I couldn't process your request right now.")

    except requests.exceptions.RequestException as e:
        # Fallback message in case of an API request error
        ai_response = "There was an error connecting to the AI service. Please try again later."

    # Send the AI's response back to the user
    response_message = {"text": ai_response}
    send_message(sender_id, response_message)
