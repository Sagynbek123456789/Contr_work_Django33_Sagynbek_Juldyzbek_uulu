from django.urls import path
from webapp.views.products_views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
     ProductDeleteView
from webapp.views.reviews_views import ReviewDeleteView, ReviewUpdateView, ReviewListView, AddReviewView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add_view'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_view'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('products/<int:product_id>/add_review/', AddReviewView.as_view(), name='add_review'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),

]

# path('reviews/', ReviewListView.as_view(), name='review_list'),
# path('products/<int:product_id>/add_review/', AddReviewView.as_view(), name='add_review'),
# path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
# path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete')
# path('products/<int:pk>/add_to_cart/', ProductAddToCartView.as_view(), name='product_add_to_cart_view'),
# path('carts/', CartsView.as_view(), name='carts_view'),
# path('products/<int:pk>/delete_of_cart/', ProductDeleteOfCartView.as_view(), name='product_delete_of_cart_view'),
# path('order/add/', OrderCreateView.as_view(), name='order_add_view')