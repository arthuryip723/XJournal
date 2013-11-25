from django.http import Http404, HttpResponse
from journals.models import JournalForm, Journal
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required

# return journal list for the logged-in user
# make a public index, and then make a private index
# If it is user, show all journals, both public and private. If it is visitor, show only the public ones.
@login_required
def index(request):
#     return HttpResponse("Hello, world. You're at the journal index.")
#     return HttpResponse(request.user.username == 'su')
    journals = Journal.objects.filter(user = request.user)
#     return render_to_response('journals/index.html', {'journals': journals})
    return render(request, 'journals/index.html', {'journals': journals})

def new(request):
    if request.POST:
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            return redirect('/')
            # redirect to index
    else:
        form = JournalForm()
#     form = JournalForm()
    
#     return render_to_response('journals/new.html', {'form': form})
    return render(request, 'journals/new.html', {'form': form})

def detail(request, journal_id):
#     try:
#         journal = Journal.objects.get(pk = journal_id)
#     except Journal.DoesNotExist:
#         raise Http404
#     return render(request, 'journals/detail.html', {'journal': journal})            
    journal = get_object_or_404(Journal, pk = journal_id)
    return render(request, 'journals/details.html', {'poll': journal})

# view a journal specified by the id

# implement the crud operations

# get a pdf from journals
# write a filter for the selection of journals, i.e. from date to date, type, or even using checkbox
