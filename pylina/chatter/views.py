from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    from django import forms
    class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)

    context = { "form" : NameForm() }
    return render(request,'chatter/chatter.html',context)
    
