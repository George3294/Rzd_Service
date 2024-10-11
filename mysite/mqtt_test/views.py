import json
from django.http import JsonResponse
from . mqtt_client import client
from. import mqtt_client
def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['message'])
    return JsonResponse({'rc': rc,'mid': mid})