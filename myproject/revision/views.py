from django.shortcuts import render,get_object_or_404

from .models import Movie
def movie_list(request):
    movies = Movie.objects.all()
    context ={'movies':movies}
    return render(request,"revision/movie_list.html",context)
def movie_details_view(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {'movie':movie}
    return render(request,"revision/movie_detail.html",context)
# Create your views here.
