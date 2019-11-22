from django.shortcuts import render, redirect
from .forms import MessagesForm
from .models import Note
# Create your views here.


def index(request):
    context = {}
    context['note'] = Note.objects.last()
    context['form'] = MessagesForm()
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            return



    return render(request, 'index.html', context)