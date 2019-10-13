from django.shortcuts import render
from django.http import HttpResponse
from .models import Photos,Category,Location
import pyperclip

def page(request):
    imaje = Photos.objects.all()
    locating = Location.objects.all()
    return render(request, 'all-photos/index.html',{"imaje":imaje,"locating":locating})


def search_results(request):
    if 'cate' in request.GET and request.GET['cate']:
        search = request.GET.get("cate")
        searched = Photos.search_by_cate(search)
        
        backend = f"{search}"
        
        return render(request, 'all-photos/search.html',{"backend":backend,"category":searched})
    
    else:
        backend = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"backend":backend})

def location(request):
    if 'location' in request.GET and request.GET['location']:
        filters = request.GET.get('location')
        found = Photos.filter_loca(filters)
        message = f'{filters}'
        locations = Location.objects.all()
        return render(request,'all-photos/personal.html',{"message":message,"found":found,"locations":locations})

# def pyperclip_link(request,id):
#     pick = Photos.objects.all()
#     single= Photos.objects.get(id = id)
#     pyperclip.copy('http//127.0.0.1:8000'+single.image.url)
#     pyperclip.paste()
#     return render(request, 'all-photos/index.html',{"pick":pick})

def image_id(request,id):
    try:
        single= Photos.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    
    return render(request,"all-photos/pick-posts.html", {"photos":single.id})