from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
from django.views.decorators.csrf import csrf_exempt
#from ttt.models import UploadedFile
#from ttt.forms import Fileform

import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file



def handle_uploaded_file(f):
    with open('templates/uploads/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        if request.FILES['file'].name.endswith('.xls'):
        	handle_uploaded_file(request.FILES['file'])
        	#return HttpResponseRedirect(request.FILES['file'].name)
        	return HttpResponseRedirect('/success/')	
        else:
        	return HttpResponse("Upload an xls file")
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>IT WORKS!!! The time is : %s.</body></html>" % now
    return HttpResponse(html)

def uuu(request):
    t = get_template('ttt/uuu.html')
    html = t.render(Context())
    return HttpResponse(html)

def chart(request):
    t = get_template('ttt/chart.html')
    html = t.render(Context())
    return HttpResponse(html)

def ajax(request):
    t = get_template('ttt/ajax.html')
    html = t.render(Context())
    return HttpResponse(html)

def line(request):
    t = get_template('ttt/line.html')
    html = t.render(Context())
    return HttpResponse(html)

def aj(request):
    t = get_template('ttt/aj.html')
    html = t.render(Context())
    return HttpResponse(html)

def linechart(request):
    t = get_template('ttt/linechart.html')
    html = t.render(Context())
    return HttpResponse(html)

def piechart(request):
    t = get_template('ttt/piechart.html')
    html = t.render(Context())
    return HttpResponse(html)

def combined(request):
    t = get_template('ttt/combined.html')
    html = t.render(Context())
    return HttpResponse(html)

def lctest(request):
    t = get_template('ttt/lctest.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def ratiometer(request):
    t = get_template('ttt/ratiometer.html')
    html = t.render(Context())
    return HttpResponse(html)

def histogram(request):
    t = get_template('ttt/histogram.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def dash(request):
    t = get_template('ttt/dash.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def consumer(request):
    t = get_template('ttt/consumer.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def product(request):
    t = get_template('ttt/product.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def slider(request):
    t = get_template('ttt/slider.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def performance(request):
    t = get_template('ttt/performance.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def performance(request):
    t = get_template('ttt/performance.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def add_to_cart(request):
    t = get_template('ttt/add_to_cart.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def buy(request):
    t = get_template('ttt/buy.html')
    html = t.render(Context())
    return HttpResponse(html)

def view(request):
    t = get_template('ttt/view.html')
    html = t.render(Context())
    return HttpResponse(html)   
    
def pie_cat(request):
    t = get_template('ttt/pie_cat.html')
    html = t.render(Context())
    return HttpResponse(html)   
    
def tt_admin(request):
    t = get_template('ttt/tt_admin.html')
    html = t.render(Context())
    return HttpResponse(html) 
    
def upload(request):
    t = get_template('ttt/upload.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def success(request):
    #t = get_template('ttt/upload.html')
    #html = t.render(Context())
    return HttpResponse("Upload Successful")          
#class UploadView(FormView)
#	template_name='main/upload_form.html'
#	form_class=FileForm
#	
#	def form_valid(self,form):
#		uploadedfile=UploadedFile(
#			upfile=self.get_form_kwargs().get('files')['upfile'])
#		uploadedfile.save()
#		self.id=uploadedfile.id
#		return HttpResponseRedirect(self.get_success_url())
#		
#	def get_success_url(self):
#		return reverse('uploadedfile',kwargs={'pk':self.id})



