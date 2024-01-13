from django import forms
# from webapp.models import Category, Product, Order
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image']
        widgets = {
            'types': forms.CheckboxSelectMultiple()
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'product', 'text', 'rating', 'is_moderated']

#
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('title', 'descriptions', 'price', 'image', 'quantity', 'category')
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         title_old = self.initial.get('title')
#         if not title_old or title !=title_old:
#             if Product.objects.filter(title=title).exists():
#                 raise forms.ValidationError('Продукт с таким названием существует')
#             return title
#
#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ('name', 'address', 'telephone')