from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Status, Estate, Person, LandPlot
from .forms import StatusForm, EstateForm, PersonForm, LandPlotForm


def index(request):
    landPlot = LandPlot.objects.all()
    return render(request, "index.html", {'landPlot': landPlot})


def createLandPlot(request):
    if request.method == "POST":
        form = LandPlotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = LandPlotForm()
    return render(request, "createLandPlot.html", {'form': form})


def displayStatus(request):
    status = Status.objects.all()
    return render(request, "displayStatus.html", {'status': status})


def createStatus(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayStatus/")
    else:
        form = StatusForm()
    return render(request, "createStatus.html", {'form': form})


def displayEstate(request):
    estate = Estate.objects.all()
    return render(request, "displayEstate.html", {'estate': estate})


def createEstate(request):
    if request.method == "POST":
        form = EstateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayEstate/")
    else:
        form = EstateForm()
    return render(request, "createEstate.html", {'form': form})


def displayPerson(request):
    person = Person.objects.all()
    return render(request, "displayPerson.html", {'person': person})


def createPerson(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/displayPerson/")
    else:
        form = PersonForm()
    return render(request, "createPerson.html", {'form': form})
