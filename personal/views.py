from django.shortcuts import render
from django.http import HttpResponse
from .models import Photos,Category,Location

def page(request):
    imaje = Photos.objects.all()
    return render(request, 'all-photos/index.html',{"imaje":imaje})


def search_results(request):
    if 'cate' in request.GET and request.GET['cate']:
        search = request.GET.get("cate")
        searched = Photos.search_by_cate(search)
        
        backend = f"{search}"
        
        return render(request, 'all-photos/search.html',{"backend":backend,"category":searched})
    
    else:
        backend = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"backend":backend})

def locator(request):
    if 'locations' in request.GET and request.GET['locations']:
        location = request.GET.get('locations')
        found = Photos.filter_loca(location)
        message = f'{location}'
       
        return render(request,'all-photos/personal.html',{"message":message,"location":found})
    else:
        message = "No selection made"
        return render(request,'all-photos/personal.html',{"message":message})


def image(request,id):
    try:
        single= Photos.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    namu=f'{single.name}'
    
    return render(request,"all-photos/pick-posts.html", {"namu":namu,"photos":single})