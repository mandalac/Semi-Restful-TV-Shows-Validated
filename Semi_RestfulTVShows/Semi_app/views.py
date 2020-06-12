from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return redirect('/shows')


def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)


def add_show_page(request):
    return render(request, 'add_a_show.html')


def create_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                            release_date=request.POST['release_date'], description=request.POST['description'])
        messages.success(request, 'Show is added')
    return redirect('/shows')


def view_show(request, show_id):
    context = {
        'shows': Show.objects.get(id=show_id)
    }
    return render(request, 'view_show.html', context)


def edit_page(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)


def update_show(request, show_id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
    return redirect(f'/shows/{show_id}')


def delete(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')
