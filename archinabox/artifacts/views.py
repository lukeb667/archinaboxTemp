from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import ArtifactModel
from .models import Filter

# Create your views here.
def artifacts(request):
    myartifacts = ArtifactModel.objects.all().values()
    myfilters = Filter.objects.all()

    template = loader.get_template('artifact.html')
    context = {
        'myartifacts': myartifacts,
        'myfilters': myfilters,
    }
    return HttpResponse(template.render(context, request))

def stlViewer(request):
    myartifacts = ArtifactModel.objects.all().values()
    template = loader.get_template('stlViewer.html')
    context = {
        'myartifacts': myartifacts,
    }
    return HttpResponse(template.render(context, request))
    