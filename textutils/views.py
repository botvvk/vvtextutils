# i have created this  file - vivek
from django.http import HttpResponse
from django.shortcuts import render



def index (request):
    return render(request, 'index.html',)


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # get the check box values
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newline_remover=request.POST.get('newlineremover', 'off')
    char_count=request.POST.get('charcount', 'off')



    if removepunc == "on":
        punctuation=''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed+=char

        params={'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        djtext=analyzed
    # # analyize the text
    #     return render(request, 'analyze.html',params)
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'captial letters', 'analyzed_text': analyzed}
        djtext=analyzed

        #     # analyize the text
        # return render(request, 'analyze.html', params)

    if newline_remover=='on':
        analyzed=''
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+=char
        params={'purpose':'New line remover', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if char_count=='on':
        count=0
        for char in djtext:
            if char!=' ':
                count+=1

        params={'purpose':'char count', 'num_char':'char_count is '+str(count),  'analyzed_text': analyzed }
        djtext=analyzed


    if (removepunc!='on' and newline_remover!='on' and char_count!='on' and fullcaps!='on'):
        return HttpResponse('please select the  operations')


    return render(request, 'analyze.html', params)













