# I have created this File - Dhara
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, 'index2.html')
    
def about(request):
    
    return render(request, 'indexAboutUs.html')
    
def contact(request):
    
    return render(request, 'contactUs.html')
    

def analyze(request):
        djtext=(request.POST.get('text', 'default'))
        
        removepunc=(request.POST.get('removepunc', 'off'))
        fullcaps=(request.POST.get('fullcaps', 'off'))
        nlremover=(request.POST.get('nlremover', 'off'))
        spremover=(request.POST.get('spremover', 'off'))
        countwords=(request.POST.get('countwords', 'off'))
        
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char.upper()
                    
                    
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            djtext = analyzed
            # return render(request, 'analyze2.html', params)

        if fullcaps == "on":
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()    
            params = {'purpose': 'CAPITALIZED letters', 'analyzed_text': analyzed}
            djtext = analyzed
            # return render(request, 'analyze2.html', params)
       
        if nlremover == "on":
            analyzed = ""
            for char in djtext:
                if char !="\n" and char !="\r":
                    analyzed = analyzed + char
            params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
            djtext = analyzed
            # return render(request, 'analyze2.html', params)
        
        if countwords == "on":
            analyzed = ""
            for char in djtext:
                analyzed = len(djtext)
            
            params = {'purpose': 'Total counted words', 'analyzed_text': analyzed}
            djtext = analyzed
            # return render(request, 'analyze2.html', params)
        
        if spremover == "on":
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index+1] == " "):    
                    analyzed = analyzed + str(char) 
                    
            params = {'purpose': 'removed extra spaces', 'analyzed_text': analyzed}
            djtext = analyzed

        if(removepunc != "on" and fullcaps != "on" and nlremover != "on" and countwords != "on" and spremover != "on"):
            return HttpResponse("<h2>Error! You didn't ticked the checkbos with your DUMB ass</h2>")

        return render(request, 'analyze2.html', params)



# def removepunc(request):
#     djtext=(request.GET.get('text', 'default'))
#     print(djtext)
#     return HttpResponse("remove punc  <a href='/'>Back</a>")

# def capfirst(request):
#     return HttpResponse("capitalize first  <a href='/'>Back</a>")

# def newlineremove(request):
#     return HttpResponse("newline remove  <a href='/'>Back</a>")

# def spaceremove(request):
#     return HttpResponse("space remove  <a href='/'>Back</a>")

# def charcount(request):
#     return HttpResponse("char count  <a href='/'>Back</a>")