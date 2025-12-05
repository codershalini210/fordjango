from django.contrib import admin
from .models import BookModel

class BookModelAdmin(admin.ModelAdmin):
    list_display=('title','author','publication_year')
    search_fields = ['title']
    list_filter=['publication_year','author']
    sortable_by = ['title']
admin.site.register(BookModel,BookModelAdmin)
# Register your models here.
