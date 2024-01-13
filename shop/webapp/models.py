from django.contrib.auth.models import User
from django.db import models
from webapp.validate_char_field import validate_summary_not_empty, validate_description_length


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название', validators=[validate_summary_not_empty])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', validators=[validate_description_length])
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='Картинка')


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Товар')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Оценка')
    is_moderated = models.BooleanField(default=False, verbose_name='Промодерировано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    def __str__(self):
        return f"{self.author.username} - {self.product.name}"

    class Meta:
        ordering = ['-created_at']


# class Cart(models.Model):
#     product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='products',
#                                 verbose_name='Продукт')
#     quantity = models.PositiveIntegerField(default=0, verbose_name='Колличество')

