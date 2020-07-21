from django.shortcuts import render, redirect
from django.http import HttpResponse

from random import randint
from . import util
from .forms import CreatePageForm # dont understand why


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
    if request.method == 'POST':
        form = CreatePageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            markdownPage = util.save_entry(title, content)
            htmlPage = util.markdownToHtmlConverter(title)
            return redirect('encyclopedia:entryPage', title=title)
    else:
        form = CreatePageForm()
    return render(request, "encyclopedia/createpage.html", {'form': form})

def randomPage(request):
    pageTitleList = util.list_entries()
    randomIndex = randint(0, len(pageTitleList) - 1)
    randomPageTitle = pageTitleList[randomIndex]
    return redirect('wiki/' + randomPageTitle)

