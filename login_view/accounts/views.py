from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,FormView
from django.views.generic.base import TemplateView,View
from .forms import RegistForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class RegisterUserView(CreateView):
    template_name= 'regist.html'
    form_class = RegistForm


class UserLoginView(FormView):
    template_name = 'user_login.html'
    form_class = UserLoginForm

    def post(self,request,*args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
        return redirect('accounts:home')

class UserLogoutView(View):
    
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect('accounts:user_login')