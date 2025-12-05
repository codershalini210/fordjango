from django.shortcuts import render
from .models import BookModel
def book_list_view(request):
    books = BookModel.objects.all()
    context = {'all_books':books}
    return render(request,'activity/booklist.html',context)
# Create your views here.
