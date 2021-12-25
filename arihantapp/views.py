import json
import os

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from arihantapp.utils import handle_uploaded_file
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from arihantapp.forms import MyForm

from .models import MyData

@csrf_exempt
def uploadFile(request):
    if request.method == 'POST':
        student = MyForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            filename = request.FILES['file'].name
            if not filename.lower().endswith(('.json', )):
                return JsonResponse({'message': 'Not a valid file'}, status=400)
            if not request.user.is_authenticated:
                return JsonResponse({'message': 'login required'}, status=400)
            file = open(os.path.join(settings.MEDIA_ROOT, filename))
            data = json.load(file)
            for i in data:
                MyData.objects.get_or_create(title = i['title'], body=i['body'], userid=i['id'],user=request.user)
            queryset = MyData.objects.all().values()
            return render(request, 'jsonData.html', {'queryset': queryset})
            #return HttpResponse(queryset)
    else:
        student = MyForm()
        return render(request,"index.html",{'form':student})