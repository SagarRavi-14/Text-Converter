#i made this file -Sagar
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")


def analyzed(request):
    djtext= request.POST.get('text','default')
    removepun = request.POST.get('removepun','off')
    caps = request.POST.get("caps",'off')
    newline = request.POST.get("newline","off")
    extraspace = request.POST.get("extraspace","off")
    charcount = request.POST.get("charcount","off")
    analyzedtext=""
    punct = '''@#$%^*.";/.,\-=.?><:'"“”'''
    if removepun=='on' and len(djtext)>0:
        for char in djtext:
            if char not in punct:
                analyzedtext = analyzedtext + char
        params ={"purpose":"Remove Punctuation","analyztext":analyzedtext}
        djtext = analyzedtext

    if caps =="on" and len(djtext)>0:
        analyzedtext=""
        for char in djtext:
                analyzedtext = analyzedtext + char.upper()
        params ={"purpose":"Full Captial","analyztext":analyzedtext}
        djtext = analyzedtext

    if newline=='on':
        analyzedtext=""
        for char in djtext:
            if char !=  "\n" and char != "\r":
                flag=0
                analyzedtext = analyzedtext + char

            elif  (char == "\n" or char == "\r") and flag==0:
                analyzedtext = analyzedtext + " "
                flag = 1

        params ={"purpose":"Remove New line","analyztext":analyzedtext}
        djtext = analyzedtext


    if extraspace =='on':
        analyzedtext = ""
        li = djtext.split(" ")
        for ele in li:
            if ele!="":
               analyzedtext =analyzedtext + ele +" "
        params = {"purpose": "Extra Space Remover", "analyztext": analyzedtext}
        djtext = analyzedtext

    if  charcount=="on":
        count = 0

        for char in djtext:
            if char!=" ":
                count = count + 1
        params = {"purpose": "Count Character","Note":"Note: It not count spaces" ,"Note2":"Number of character in your text is ","Text":djtext,"analyztext":count}



    elif (removepun!="on" and caps!="on" and newline!='on' and charcount!="on" and extraspace!='on'):
        return HttpResponse("error")

    return render(request, 'analyzer2.html', params)

