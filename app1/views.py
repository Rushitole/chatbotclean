import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


def chat_page(request):
    return render(request, "chat.html")


@csrf_exempt
def chat_stream(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            response = requests.post(
    "http://127.0.0.1:11434/api/generate",
    json={
        "model": "tinyllama:latest",
        "prompt": user_message,
        "stream": False,
        "options": {
            "num_predict": 100,   # limit output length
            "temperature": 0.7
        }
    },
    timeout=60
)

            print("Status Code:", response.status_code)
            print("Raw Text:", response.text)

            if response.status_code == 200:
                result = response.json()
                bot_reply = result.get("response", "")
                return JsonResponse({"reply": bot_reply})

            else:
                return JsonResponse({"reply": "Ollama error"})

        except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({"reply": f"Error: {str(e)}"})

    return JsonResponse({"error": "Invalid request"}, status=400)