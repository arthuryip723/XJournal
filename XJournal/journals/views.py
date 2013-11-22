from django.http import HttpResponse
from journals.models import JournalForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

# return journal list for the logged-in user
# make a public index, and then make a private index
# If it is user, show all journals, both public and private. If it is visitor, show only the public ones.
@login_required
def index(request):
#     return HttpResponse("Hello, world. You're at the journal index.")
    return HttpResponse(request.user.username == 'su')

def new(request):
    if request.POST:
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to index
    else:
        form = JournalForm()
    
    return render_to_response('journals/new.html', {'form': form})

# view a journal specified by the id

# implement the crud operations

# get a pdf from journals
# write a filter for the selection of journals, i.e. from date to date, type, or even using checkbox