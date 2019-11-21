from django.shortcuts import render, redirect
from .forms import MessagesForm
# Create your views here.


def index(request):
    context = {}
    context['form'] = MessagesForm()
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            return



    return render(request, 'index.html', context)