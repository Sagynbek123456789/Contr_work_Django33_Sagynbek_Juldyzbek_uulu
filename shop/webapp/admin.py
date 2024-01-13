from django.contrib import admin
from webapp.models import Product, Review


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(OrderProduct)
# class OrderProductAdmin(admin.ModelAdmin):
#     pass
#
