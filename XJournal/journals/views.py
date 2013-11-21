from django.http import HttpResponse
from journals.models import JournalForm
from django.shortcuts import render_to_response

def index(request):
#     return HttpResponse("Hello, world. You're at the journal index.")
    return HttpResponse(request.user.username == 'su')

def new(request):
    if request.POST:
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = JournalForm()
    
    return render_to_response('journals/new.html', {'form': form})