
import os
import random
import requests
from flask import Flask, request

app = Flask(__name__)

PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

TAMANNA_IMAGES = [
    "https://i.ibb.co/hx9sXqtP/5811913392800251527-121.jpg",
    "https://i.ibb.co/CKzvk500/358186624-699979911651420-1803425898810046622-n.jpg",
    "https://i.ibb.co/DHB8q29m/369762586-683307257101058-5371590143009653443-n.jpg",
    "https://i.ibb.co/Q799kqZv/378089749-1030895868056823-2896055998058229651-n.jpg",
    "https://i.ibb.co/SDKzjk9t/378089762-3480291812301213-3693020438261947084-n.jpg",
    # ... (and so on for 1000+ links; truncated for space here)
]

def send_image(recipient_id, image_url):
    data = {
        "recipient": {"id": recipient_id},
        "message": {
            "attachment": {
                "type": "image",
                "payload": {"url": image_url, "is_reusable": True}
            }
        }
    }
    headers = {"Content-Type": "application/json"}
    url = f"https://graph.facebook.com/v17.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    requests.post(url, json=data, headers=headers)

@app.route("/", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verification token"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    for entry in data.get("entry", []):
        for messaging_event in entry.get("messaging", []):
            if "message" in messaging_event and "text" in messaging_event["message"]:
                sender_id = messaging_event["sender"]["id"]
                message_text = messaging_event["message"]["text"].lower()
                if "tamanna" in message_text:
                    img_url = random.choice(TAMANNA_IMAGES)
                    send_image(sender_id, img_url)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
