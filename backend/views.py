from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={}
    template=loader.get_template('app/index.html')

    return HttpResponse(template.render(context,request))

def other_html(request):
    context={}
    load_template=request.path.split('/')[-1]+'.html'
    # print("temp:"+load_template)
    # return HttpResponse(load_template)
    template=loader.get_template('app/'+load_template)

    return HttpResponse(template.render(context,request))