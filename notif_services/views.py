import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

#The link should be replaced to get the TEAMS incoming webhook url (The actual link is for the slack incoming webhook url)
TEAMS_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

def home(request):
    return render(request, 'notif_services/home.html')

def receive_notification(request):
    if request.method == 'POST':
        data = request.POST.dict()
        notification_type = data.get('Type')
        notification_name = data.get('Name')
        notification_description = data.get('Description')
        if notification_type == 'Warning':
            message = f"**{notification_name}**\n{notification_description}"
            payload = {"text": message}
            response = requests.post (TEAMS_WEBHOOK_URL, json=payload)
            if response.status_code == 200:
                return JsonResponse({'message': 'Notification forwarded to Microsoft Teams'})
            else:
                return JsonResponse({'error': 'Failed to forward notification to Microsoft Teams'}, status=200)
        else:
            return JsonResponse({'message': 'Notification not forwarded'}, status = 200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status = 405)

