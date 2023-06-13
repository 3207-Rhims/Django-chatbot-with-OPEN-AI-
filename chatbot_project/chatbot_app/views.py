import openai
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse

openai.api_key = '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'

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        response = openai.Completion.create(
            model = "davinci:ft-century-2023-06-12-10-54-51",
            #engine='text-davinci-003',
            prompt=message,
            max_tokens=100,
            n=1,
            stop=[" END"],
            temperature=0.7
        )
        reply = response.choices[0].text.strip()
        return JsonResponse({'message': reply})


# Replace the following placeholders with your actual Twilio credentials and WhatsApp numbe

def chatbot(request):
    return render(request, 'chatbot.html')
