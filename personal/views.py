from django.shortcuts import render
from django.http import HttpResponse
from .models import Photos,Category,Location

def page(request):
    imaje = Photos.objects.all()
    return render(request, 'all-photos/index.html',{"imaje":imaje,})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        searched_categories = Photos.search_by_category(search_term)
        
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html',{"message":message,"categories":searched_categories})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def photos(request,photos_id):
    try:
        photos = Photos.objects.get(id = photos_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/index.html", {"photo":photo})
