from django.contrib import admin
from mainapp.models import (BookCategory, Author, Book)
admin.site.register(BookCategory)
admin.site.register(Author)
admin.site.register(Book)

