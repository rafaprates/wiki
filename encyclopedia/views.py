from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from random import randint
from . import util
from .forms import CreatePageForm, EditPageForm # dont understand why


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    print(title)
    if request.method == "GET":
        if title in util.list_entries():    
            templateBodyContent = util.markdown_to_html_coverter(title)
            context = { 'title': title,
                        'bodyContent': templateBodyContent}
            return render(request, "encyclopedia/page.html", context)
        else:
            return HttpResponse('<h1>404. Page not found.<h1>')
    elif request.method == "POST":
        print("@@@@@@@@@@@@@@@@@@@@@@@")
        #content = util.get_entry(title)
        #data = {"content": content}
        #form = EditPageForm(initial=data)
        print(title)
        return redirect("encyclopedia:editPage", title)

def create_new_page(request):
    if request.method == 'POST':
        form = CreatePageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            markdownPage = util.save_entry(title, content)
            htmlPage = util.markdown_to_html_coverter(title)
            return redirect('encyclopedia:entryPage')
    else:
        form = CreatePageForm()
    return render(request, "encyclopedia/createpage.html", {"form": form})


def edit_existing_page(request, title):
#    title = request.path
    print(title)
#    title = title.replace("wiki/", '')
#    content = util.get_entry(title)
    data = {"content": content}
    form = EditPageForm(initial=data)
    #page = util.get_entry('CSS')
    return render(request, "encyclopedia/editpage.html", {"form": form})


def select_random_page(request):
    pageTitleList = util.list_entries()
    randomIndex = randint(0, len(pageTitleList) - 1)
    randomPageTitle = pageTitleList[randomIndex]
    return redirect('wiki/' + randomPageTitle)

