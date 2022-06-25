import http
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Advertisement


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def accept_advertisement(request):
    if request.method == "POST" and request.user.is_staff:
        try:
            if request.body:
                body = json.loads(request.body)
                if body["status"] == "published":
                    Advertisement.objects.get(pk=body["id"]).set_accept_status()
                    return JsonResponse(data={"status": "success"}, status=http.HTTPStatus.OK)
        except:
            return JsonResponse(data={"status": "failed"}, status=http.HTTPStatus.NOT_FOUND)


def reject_advertisement(request):
    if request.method == 'POST' and request.user.is_staff:
        try:
            if request.body:
                body = json.loads(request.body)
                if body['status'] == 'rejected':
                    Advertisement.objects.get(pk=body['id']).set_reject_status()
                    return JsonResponse(data={'status': 'success'}, status=http.HTTPStatus.OK)
        except:
            return JsonResponse(data={'status': 'failed'}, status=http.HTTPStatus.NOT_FOUND)
