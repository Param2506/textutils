from email import charset
from email.policy import default
from string import punctuation
from tempfile import template
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request , "index.html")

def info(request):
    djtext=request.POST.get('text', 'default')
    password=request.POST.get("password",)
    option1=request.POST.get("remove", "off")
    option2=request.POST.get("switch", "off")
    option3=request.POST.get("extra" , "off")
    if djtext=="":
        djtext="No text"
    if password=="":
        password=""
    c=""
    punc='''?/"':;.<>(),}{][\|+=_-!~#$@&*"^%'''
    if(option1=="on"):
        for i in djtext:
            if i not in punc:
                c=c+i
    
        params= {'analyze_text': c , 'pass': password}
        djtext=c

    if(option2=="on"):
        c=djtext.upper()
    
        params= {'analyze_text': c , 'pass': password}
        djtext=c

    if(option3=="on"):
        c=""
        for index ,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                c=c+char
        params= {'analyze_text': c , 'pass': password}
    
    return render(request, 'resultent.html' , params)



    