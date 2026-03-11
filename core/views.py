from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.models import Testing
from core.serializers import TestingSerializer


def testing_view(request):
    qs = Testing.objects.all()
    serializer = TestingSerializer(qs, many=True)
    return JsonResponse(serializer.data, safe=False)


def testing_detail_view(request, id):
    testing = get_object_or_404(Testing, id=id)
    serializer = TestingSerializer(testing)
    return JsonResponse(serializer.data)


def health_check(request):
    return JsonResponse({'status': 'ok'})
from django.shortcuts import render

# Create your views here.
