from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, title):
    if title in util.list_entries():    
        templateBodyContent = util.markdownToHtmlConverter(title)
        context = { 'title': title,
                    'bodyContent': templateBodyContent}
        return render(request, "encyclopedia/page.html", context)
    else:
        return HttpResponse('<h1>404. Page not found.<h1>')

def createNewPage(request):
    return render(request, "encyclopedia/newpage.html")

def randomPage(request):
    pageTitleList = util.list_entries()
    randomIndex = randint(0, len(pageTitleList) - 1)
    randomPageTitle = pageTitleList[randomIndex]
    return redirect('wiki/' + randomPageTitle )

