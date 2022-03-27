from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from . import forms
from .password_class import Password
# Create your views here.
class home_view(TemplateView):
    template_name = "pages/home.html"
    def get(self,request):
        form = forms.passwordForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form = forms.passwordForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data["length"]
            lower = form.cleaned_data["lower"]
            upper = form.cleaned_data["upper"]
            digits = form.cleaned_data["digits"]
            symbols = form.cleaned_data["symbols"]
            p1 = Password(lower, upper, digits, symbols, length)
            password = p1.create()
            print(password)
            args = {
                "password":password,
                "form":form,
            }
            return render(request,self.template_name,args)
        else:
            args = {
                "password":"",
                "form":form,
            }
            return render(request,self.template_name,args)