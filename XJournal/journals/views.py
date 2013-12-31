from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, \
    render_to_response
from django.utils import timezone
from django.views import generic
from django.core.servers.basehttp import FileWrapper
from django.core.files.temp import NamedTemporaryFile

from journals.models import JournalForm, Journal
import os, StringIO

# return journal list for the logged-in user
# make a public index, and then make a private index
# If it is user, show all journals, both public and private. If it is visitor, show only the public ones.
@login_required
def index(request):
#     return HttpResponse("Hello, world. You're at the journal index.")
#     return HttpResponse(request.user.username == 'su')
    journals = Journal.objects.filter(user=request.user)
#     return render_to_response('journals/index.html', {'journals': journals})
    return render(request, 'journals/index.html', {'journals': journals})

@login_required
def new(request):
    if request.POST:
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.pub_date = timezone.now()
            journal.rev_date = timezone.now()
            journal.save()
            return redirect('/journals')
            # redirect to index
    else:
        form = JournalForm()
#     form = JournalForm()
    
#     return render_to_response('journals/new.html', {'form': form})
    return render(request, 'journals/new.html', {'form': form})

# def detail(request, journal_id):
# #     try:
# #         journal = Journal.objects.get(pk = journal_id)
# #     except Journal.DoesNotExist:
# #         raise Http404
# #     return render(request, 'journals/detail.html', {'journal': journal})            
#     journal = get_object_or_404(Journal, pk=journal_id)
#     return render(request, 'journals/detail.html', {'journal': journal})


class DetailView(generic.DetailView):
    model = Journal
    template_name = 'journals/detail.html'

def edit(request, journal_id):
#     record = Journal.objects.get(pk=journal_id)
    if request.POST:
        return redirect('/journals')
        #redirect to index?
    else:
        journal = get_object_or_404(Journal, pk=journal_id)
        form = JournalForm(instance=journal)
    return render(request, 'journals/edit.html', {'form': form})

def delete(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    pass

# view a journal specified by the id

# implement the crud operations

# get a pdf from journals
# def getPDF(request, journal_id):
def getPDF(request,):
#     journal = get_object_or_404(Journal, pk=journal_id)
    # Print the pdf
#     f = NamedTemporaryFile(suffix='.txt')
    pdf = open("test.pdf", "r+")
#     f.write(pdf.read())
#     f.flush()
#     f.write("hello world!")
#     f.flush()
#     print pdf.read()
#     print f.read()
#     f.flush()
#     buffer = StringIO.StringIO()
    response = HttpResponse(FileWrapper(pdf), content_type='application/pdf')
#     response = HttpResponse(FileWrapper(f), content_type='application/txt')
    response['Content-Disposition'] = 'attachment; filename=journal.txt'
#     os.remove("foo.txt")
    return response
#     fo = open("foo.txt", "wb")
#     fo.write("Python is a great language.\nYeah it's great!!\n");
#     return HttpResponse("Successful")


# write a filter for the selection of journals, i.e. from date to date, type, or even using checkbox
