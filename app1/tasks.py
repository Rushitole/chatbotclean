from celery import shared_task
# from openai import OpenAI
from .models import Message
# from django.conf import settings
import requests

@shared_task
def process_chat(message_id, user_message):


    response =requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"phi3:mini",
            "prompt":user_message,
            "stream":False
        }

    )

    bot_reply = response.json()["response"]

    message = Message.objects.get(id=message_id)
    message.bot_response = bot_reply
    message.save()