
import os
import random
import requests
from flask import Flask, request

app = Flask(__name__)

PAGE_ACCESS_TOKEN = os.getenv('EAAQ3tNx3kz0BO4Sz6Hb79eZBy19kfmb2iNgvZCZBxeNVkORZC9ng4HQ1KGgUkePilf1jZBfE2bY67uPNyMqruKDKn9jZATuPkeL9W2iZCBBj6INLyhebL77KZCqhZAeAek8HZB1xZC9oPYUqf5keZC7W6FNZC1aNNUBnD10ZAFaLZAQIyNX1mpqnfG5bHVZCRaXXBmiXLQZDZD')
VERIFY_TOKEN = os.getenv('alvibot123')

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

@app.route('/', methods=['GET', 'HEAD'])
def verify():
    return "Alvannaah Bot is live! ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
