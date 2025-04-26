import os, random, requests
from flask import Flask, request

app = Flask(__name__)

PAGE_ACCESS_TOKEN = os.getenv('EAAQ3tNx3kz0BO4Sz6Hb79eZBy19kfmb2iNgvZCZBxeNVkORZC9ng4HQ1KGgUkePilf1jZBfE2bY67uPNyMqruKDKn9jZATuPkeL9W2iZCBBj6INLyhebL77KZCqhZAeAek8HZB1xZC9oPYUqf5keZC7W6FNZC1aNNUBnD10ZAFaLZAQIyNX1mpqnfG5bHVZCRaXXBmiXLQZDZD')
VERIFY_TOKEN = os.getenv('alvibot123')

# Tamannaah Images
TAMANNA_IMAGES = [
    "https://i.ibb.co/corrected-link-1.jpg",
    "https://i.ibb.co/corrected-link-2.jpg",
    # ...(all your 1000+ links)
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
    for entry in data["entry"]:
        for messaging_event in entry["messaging"]:
            if "message" in messaging_event and "text" in messaging_event["message"]:
                sender_id = messaging_event["sender"]["id"]
                message_text = messaging_event["message"]["text"].lower()
                if "tamanna" in message_text:
                    img_url = random.choice(TAMANNA_IMAGES)
                    send_image(sender_id, img_url)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
