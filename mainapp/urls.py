from django.urls import path
from rest_framework.routers import DefaultRouter as DR
from mainapp.views import (
    BookCategoryView, AuthorView, BookView, RegistrationView, AuthorizationView
)
router = DR()
router.register('bookcategories', BookCategoryView, basename='bookcategory')
router.register('authors', AuthorView, basename='author')
router.register('books', BookView, basename='book')
urlpatterns = [
        path('reg/', RegistrationView.as_view()),
        path('aut/', AuthorizationView.as_view()),
]
urlpatterns += router.urls