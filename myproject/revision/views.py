from django.shortcuts import render,get_object_or_404
from .models import Movie
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def movie_list(request):
    object_list  = Movie.objects.all()
    
    paginator = Paginator(object_list,3) #3 movies per page
    page = request.GET.get('page')
    try:
        movies =paginator.page(page)
    except PageNotAnInteger: #if page is not a integer -> show first page
        movies = paginator.page(1)
    except EmptyPage: #if page is out of range -> show lastpage
        movies = paginator.page(paginator.num_pages)
        
    context ={'movies':movies}
    return render(request,"revision/movie_list.html",context)




def movie_details_view(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {'movie':movie}
    return render(request,"revision/movie_detail.html",context)
# Create your views here.
