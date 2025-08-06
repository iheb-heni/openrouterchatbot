from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from openai import OpenAI
from django.shortcuts import render

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

@csrf_exempt
def chat_with_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get("message")

        try:
            response = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct",
                messages=[
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response.choices[0].message.content
            return JsonResponse({"response": reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

def chat_ui(request):
    return render(request, "chat.html")