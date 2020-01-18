from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.


class Index(View):
    def get(self,request):
        return render(request, "MedWebApp/index.html", context=None)

    def post(self,request):
        pass