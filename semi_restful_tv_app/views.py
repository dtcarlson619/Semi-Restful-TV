from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, "index.html", context)

def editPage(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id),
    }
    return render(request, "update_show.html", context)

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if request.method == "POST":
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{show_id}/edit")
        else: 
            show = Show.objects.get(id=show_id)
            show.title = request.POST["title"]
            show.network = request.POST["network"]
            show.release_date = request.POST["release_date"]
            show.description = request.POST["description"]
            show.save()
            return redirect(f"/shows/{show_id}")
    
def showDetails(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id),
    }
    return render(request, "show_details.html", context)

def deleteShow(request, show_id):
    thisShow = Show.objects.get(id=show_id)
    thisShow.delete()
    return redirect("/shows")

def addShowPage(request):
    return render(request, "new_show.html")

def createShow(request):
    errors = Show.objects.basic_validator(request.POST)
    if request.method == "POST":
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new")
        else: 
            title = request.POST["title"]
            network = request.POST["network"]
            release_date = request.POST["release_date"]
            description = request.POST["description"]
            newShow = Show.oblocjects.create(title = title, network = network, release_date = release_date, description = description)
            return redirect(f"/shows/{newShow.id}")