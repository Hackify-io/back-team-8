from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import UserTIA
from django.template.loader import render_to_string
from django.core.mail import send_mail
from MedApp import settings
# Create your views here.


class Index(View):
    def get(self,request):
        return render(request, "MedWebApp/index.html", context=None)

    def post(self,request):
        pass

class SignUp(View):
    def get(self,request):
        return render(request, "MedWebApp/sign-up.html", context=None)


    def post(self, request):
        data = parse_to_dict(dict(request.POST))
        data_response = {"is_valid": False}
        user_tia = UserTIA.create_user(**data)
        if user_tia:
            data_response["is_valid"] = True
            to_email = request.POST.get("email")
            token = user_tia.token_key
            html_token = render_to_string('MedWebApp/html_includes/verification-code.html', context={"verification_code": token})
            send_mail(subject="TOKEN", message="TOKEN", html_message=html_token,
                      from_email=settings.EMAIL_HOST_USER, recipient_list=[to_email])
        return JsonResponse(data)


class Directory(View):
    def get(self,request):
        return render(request, "MedWebApp/directory.html", {"Doctors":["Armando","Roberto","Ezekiel"],
                                                       "Clinics":["Diamond_Clinic","Health Clinic"]})

    def post(self,request):
        pass

class Login(View):
    def get(self,request):
        return render(request, "MedWebApp/login.html", context=None)

    def post(self, request):
        pass


class Clinic(View):
    def get(self,request):
        return render(request, "MedWebApp/clinic.html", context=None)

    def post(self,request):
        pass

class Clinic_appointment(View):
    def get(self,request):
        return render(request, "MedWebApp/appointments.html", context=None)

    def post(self,request):
        pass

class Clinic_financial(View):
    def get(self,request):
        return render(request, "MedWebApp/financial.html", context=None)

    def post(self,request):
        pass

class Clinic_visits(View):
    def get(self,request):
        return render(request, "MedWebApp/visits.html", context=None)

    def post(self,request):
        pass


def parse_to_dict(data):
    for key in data.keys():
        data[key] = data[key][0]
    return data



def database_validator(request):
    if request.method == "POST":
        data = dict()
        if request.POST.get("email"):
            data["is_valid"] = not User.objects.filter(email=request.POST.get("email")).exists()
        elif request.POST.get("username"):
            data["is_valid"] = not User.objects.filter(username=request.POST.get("username")).exists()
        return JsonResponse(data)

def activate_user_by_token(request):
    if request.method == "POST":
        data = {"is_valid": False}
        user_tia = UserTIA.objects.filter(token_key=request.POST.get("token_key"))
        if user_tia.exists():
            user_tia.update(token_activated=True)
            data["is_valid"] = True
        return JsonResponse(data)
