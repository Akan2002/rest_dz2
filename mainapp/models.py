from django.db import models
from django.contrib.auth.models import AbstractUser

class BookCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя', null=True, blank=True)
    image = models.ImageField(upload_to='bookcategories/image/', verbose_name='Картинка')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Категория книг'
        verbose_name_plural = 'Категории книг'
class Author(AbstractUser):
    book_amount = models.CharField(max_length=120, verbose_name='Сумма книг', null=True, blank=True)
    date_birthday = models.DateField(auto_now_add=True, null=True, blank=True)
    pseudonym = models.CharField(max_length=120, verbose_name='Псевдоним', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/image/', verbose_name='Аватар', null=True, blank=True)
    book_category = models.ForeignKey(to=BookCategory, on_delete=models.CASCADE, related_name='authors', verbose_name='Категория книг', null=True, blank=True)
    def __str__(self) -> str:
        return self.username
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = verbose_name + 'ы'
class Book(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя', null=True, blank=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='books', verbose_name='автор', null=True, blank=True)
    date_of_issue = models.DateField(auto_now_add=True, verbose_name='Дата выпуска', null=True, blank=True)
    chapter_amount = models.IntegerField(default=0, verbose_name='Кол-во глав', null=True, blank=True)
    preview = models.DateField(auto_now_add=True, verbose_name='Предварительный просмотр', null=True, blank=True)
    book_category = models.ForeignKey(to=BookCategory, on_delete=models.CASCADE, related_name='books', verbose_name='Категория книг', null=True, blank=True)
    price = models.IntegerField(default=0, verbose_name='Цена', null=True, blank=True)
    discount = models.IntegerField(default=0, verbose_name='Скидка', null=True, blank=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = verbose_name + 'и'
