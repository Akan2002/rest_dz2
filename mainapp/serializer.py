from rest_framework import serializers, exceptions
from mainapp.models import (
    BookCategory, Author, Book,
)
class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = (
            'id', 'name', 'image', 
        )
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
        'id', 'book_amount', 'date_birthday', 'pseudonym', 'avatar', 'book_category',
        )
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id', 'name', 'author', 'date_of_issue', 'chapter_amount', 'preview', 'book_category', 'price', 'discount',
        )
class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 8:
            raise exceptions.ValidationError('password to short')
        elif len(value) > 8:
            raise exceptions.ValidationError('password is to long')
        return value
class AuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()