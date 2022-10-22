from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))



def addrecord(request):
   x = request.POST['first']
   y = request.POST['last']
   member = Members(firstname=x, lastname=y)
   member.save()
   return HttpResponseRedirect(reverse('index'))

def delete(request,id):
      members = Members.objects.get(id = id)
      members.delete()
      return HttpResponseRedirect(reverse('index'))
 



