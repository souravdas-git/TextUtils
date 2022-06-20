#  I have created this file - sourav
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return  render(request,'index.html')

def analyze(request):
    # Get the text
    djtext=(request.POST.get('text', 'default'))

    # Check checkbox values
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    extraspacemover=(request.POST.get('extraspacemover','off'))


    # Check which checkbox is on
    if removepunc =="on":
        # analyzed=djtext
        punctuations = '''!()-[]{};:`'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
          if char not in punctuations:
            analyzed=analyzed + char

        params={'purpose':'Removed Punctuation','analyzed_text':analyzed }
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = " "
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed = " "
        for char in djtext:
            if char !="\n" and char !="\r":
               analyzed = analyzed + char
        params = {'purpose': 'Removed newline', 'analyzed_text': analyzed}
        djtext=analyzed
    if(extraspacemover=="on"):
        analyzed = " "
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spacemover', 'analyzed_text': analyzed}
        djtext=analyzed
    if(removepunc !="on" and fullcaps !="on" and newlineremover !="on" and extraspacemover !="on"):
        return HttpResponse("please select the operation")

    return render(request, 'analyze.html', params)




