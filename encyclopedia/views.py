from django.shortcuts import render
from django.http import HttpResponse
from random import randint

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, title):
    return HttpResponse(title)

def createNewPage(request):
    return render(request, "encyclopedia/newpage.html")

def randomPage(request):
    pageTitleList = util.list_entries()
    randomIndex = randint(0, len(pageTitleList) - 1)
    randomPageTitle = pageTitleList[randomIndex]

    context = {'title': randomPageTitle}

    return render(request, "encyclopedia/randompage.html", context)
