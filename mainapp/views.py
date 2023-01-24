from django.shortcuts import render
from mainapp.serializer import(
    BookCategorySerializer, AuthorSerializer, BookSerializer, RegistrationSerializer, AuthorizationSerializer,  
)
from mainapp.models import(
    BookCategory, Author, Book, 
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import action

class BookCategoryView(ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

    @action(methods=[ 'post', ], detail=True, serializer_class = BookSerializer,
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,))
    def add_book(self, request, *args, **kwargs):
        bookcategory = self.get_object()
        user = request.user
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        book = Book.objects.create(
            bookcategory = bookcategory,
            name = data.get ('name'),
            author = user,
            date_of_issue = data.get ('data_of_issue'),
            chapter_amount = data.get ('chapter_amount'),
            preview = data.get ('preview'),
            price = data.get ('price'),
            discount = data.get ('discount'),
        ) 
        return Response(BookSerializer(book).data)
    
class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RegistrationView(APIView):
    def post (self, request):
        serializer = RegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if User.objects.filter(username = username).exists():
            return Response({'message': 'Username with such username is already exist'})
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
        )
class AuthorizationView(APIView):
    def post(self, request):
        serializer = AuthorizationSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = data.get('username')
        password = data.get('password')

        if User is not None:
            if check_password(password, User.password):
                token, _=Token.objects.get_or_create(user=User)
                return Response({'token': token.key})
            return Response({'error': 'Password is not vallid'}, status=400)
        return Response({'error': 'username is not vallid'}, status=400)