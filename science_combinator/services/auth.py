from base import BaseService
from profile import ProfileService
from django.contrib.auth import logout, login, authenticate


class AuthService(BaseService):

    def login(self, data, request):

        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise Exception("Your username or password is wrong.")

        login(request, user)

    def register(self, data, request):

        if data["password"] != data["password_confirm"]:
            raise Exception("Your password doesn't match.")

        try:
            user = ProfileService().new(username=data["username"])            
            user.set_password(data["password"])
            user.save()
        except:
            raise Exception("The username has already been taken.")

        self.login(data, request)
        
    def logout(self, request):

        logout(request)