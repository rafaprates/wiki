import re, markdown2

from django.shortcuts import redirect
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
        

def markdown_to_html_coverter(title):
    """
    Retrivies an entry in markdown format by its title and returns the HTML equivalent.
    """
    html = ''
    with open(f"./entries/{title}.md") as f:
        for line in f:
            html += markdown2.markdown(line) # converts each line to html.
    return html


def match_for_entries(getParameter):

    title = re.compile(getParameter, re.IGNORECASE)
    matches = []
    
    for entry in list_entries():
        match = title.search(entry)
        if match:
            matches.append(entry)
    return matches


def listen_for_search(getParameter):
    """
    Returns True if the user is trying to search for a page.
    """
    if bool(getParameter): # if the dictionary is empty, the user is not searching for anything.
        return True
    else:
        return False


def search_for_page(getParameter):
    """
    Searches for a page based on the value of the GET Parameter. 
    """
    value = getParameter['q'] # retrieves the value of the q GET parameter.
    if value in list_entries():
        return redirect("encyclopedia:entryPage", title=value)
    else:
        return redirect("encyclopedia:searchResults", searchTerm=value)