#I haver created this file-jash jain
import os
from django.http import HttpResponse

#for displatying one.txt file in the same directory as views.py on the homepage
# def index(request):
#     html2 = open(os.path.dirname(os.path.realpath(__file__)) + '\one.txt', "r")
#     return HttpResponse(html2,content_type='text/plain')

#to add a link
# def index(request):
#     return HttpResponse(''' <h1>Jash</h1><a href="https://thepìratebay.com/proxy/go.php?url=
#     torrent/12499831/MICROSOFT_Office_PRO_Plus_2016_v16.0.4266.1003_RTM___Activator"> First Site</a> ''')
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    #get the text
    djtext=request.POST.get('text1','default')
    #check the checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    #and analyse the text
    analysed=''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #checkk which checkbox is on
    if removepunc=='on':
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose':'Removed Punctutation','analysed_text':analysed}
        # return render(request,'analyse.html',params)
        djtext=analysed
    if fullcaps=='on':
        analysed=''
        for char in djtext:
            analysed=analysed+char.upper()
        params={'purpose':'Changed to upper text','analysed_text':analysed}
        #return render(request,'analyse.html',params)
        djtext=analysed
    if newlineremover=='on':
        analysed=''
        for char in djtext:
            if char!='\n' and char !='\r':
                analysed=analysed+char
        params={'purpose':'Removed New lines','analysed_text':analysed}
        djtext=analysed
        #return render(request,'analyse.html',params)
    if extraspaceremover=='on':
            analysed=''
            for index,char in enumerate(djtext):
                if not(djtext[index]==' ' and djtext[index+1]==' '):
                    analysed=analysed+char
            params={'purpose':'Removed Extra space','analysed_text':analysed}
            #return render(request,'analyse.html',params)
            djtext=analysed
    if charcounter=='on':
            analysed=''
            analysed=len(djtext)
            params={'purpose':'Removed Extra space','analysed_text':analysed}
    if(removepunc!='on' and extraspaceremover!='on' and charcounter!='on' and newlineremover!='on' and fullcaps!='on'):
        return HttpResponse("Please select nay operation and try again")
    return render(request,'analyse.html',params)
