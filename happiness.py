import requests, random
import os

# --- Keys ---
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

Emoji_list = ['☀️', '😊', '🌻', '🔥', '🥰', '💖', '🌟', '✨', '😁', '🐥', '🐧', '🐻']

# --- Fetching quote ---
def get_motivational_quote():
    api_url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json() # this converts the json input into a python list for us to use
            chosen_quote = random.choice(data)
            quote = chosen_quote['q']
            author = chosen_quote['a']
            return f'"{quote}" \n -{author}'
        else:
            return "Happiness also comes from fixing your personal projects :D"

    except Exception as e:

        return "Happiness also comes from fixing your personal projects :DD"


# --- Sending quote ---
def send_motivational_quote():
    daily_quote = get_motivational_quote()
    emoji = random.choice(Emoji_list)

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": f"{emoji} Good morning! Here is your daily pick-me-up: \n\n{daily_quote}"
    }

    response = requests.post(telegram_url, json=payload)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send:", response.text)


send_motivational_quote()

