from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from hashlib import blake2b
# Create your models here.




class UserTIA(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  #ID is already in USER class
    token_activated = models.BooleanField(default=True)
    token_key = models.CharField(max_length=8, blank=False, null=False)
    date = models.DateField(auto_now=True, auto_created=True, blank=False)

    def __str__(self):
        return "id:{} | username={} | authenticated={} | date={}".format(self.user.id,
                                                                         self.user.username,
                                                                         self.token_activated,
                                                                         self.date)

    @staticmethod
    def create_user(**kwargs):
        base_user = UserForm(data=kwargs)
        if UserTIA.validate(base_user,**kwargs):
            del kwargs["password_confirmation"]
            token_key = UserTIA.generate_token(kwargs["username"], kwargs["email"])
            base_user.save()
            user_tia = UserTIA(user=base_user.instance,token_key=token_key)
            user_tia.save()
            return user_tia
        return None

    @staticmethod
    def generate_token(username,email):
        #   MAKE AN INSTANCE OF `ActiveToken`   #
        encode_string = username + email
        encode_string = encode_string.encode()
        encrypted_code = blake2b(digest_size=4)
        encrypted_code.update(encode_string)
        return encrypted_code.hexdigest()

    @staticmethod
    def validate(base_user, **kwargs):
        return base_user.is_valid() and\
               (kwargs["password"] == kwargs["password_confirmation"]) and\
               not User.objects.filter(email=kwargs["email"]).exists()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username","email","password")

