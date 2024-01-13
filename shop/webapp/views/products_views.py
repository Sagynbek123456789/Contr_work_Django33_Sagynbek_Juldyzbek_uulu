from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    paginate_by = 5


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()  # Используйте 'reviews' вместо 'review'
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    # form_class = ProductForm
    success_url = reverse_lazy('index')

#
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixinfrom django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse, reverse_lazyfrom django.utils.http import urlencode
# from django.db.models import Qfrom .models import Products, Reviews
# from .forms import ProductsForm, ReviewsFormfrom django.views.generic import View, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
# class IndexView(ListView):
#     model = Products    template_name = 'articles/index.html'
#     context_object_name = 'articles'    paginate_by = 6
#     paginate_orphans = 3    ordering = ('-created_at',)
#     def get_queryset(self):
#         query = self.request.GET.get('q')        if query:
#             return Products.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))        else:
#             return Products.objects.all()
# class ProductsView(DetailView):
#     model = Products    template_name = 'articles/article_view.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)        context['reviews'] = self.object.reviews.all()
#         return context
#
# class ProductsCreateView(LoginRequiredMixin, CreateView):    template_name = 'articles/article_create.html'
#     model = Products    form_class = ProductsForm
#     def form_valid(self, form):
#         self.product = form.save(commit=False)        self.product.author = self.request.user
#         self.product.save()        form.save_m2m()
#         return redirect('reviewapp:article_view', pk=self.product.pk)
#
# class ProductsUpdateView(PermissionRequiredMixin, UpdateView):    template_name = 'articles/article_update.html'
#     model = Products    form_class = ProductsForm
#     permission_required = 'reviewapp.change_article'
#     def has_permission(self):        return super().has_permission() or self.request.user == self.get_object().author
#
# class ProductsDeleteView(UserPassesTestMixin, DeleteView):    template_name = 'articles/article_delete.html'
#     model = Products    success_url = reverse_lazy('reviewapp:index')
#     def test_func(self):
#         return self.request.user.has_perm('reviewapp.article_delete_view') or self.request.user == self.get_object().author
# class ReviewsCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'comments/comment_create.html'    model = Reviews
#     form_class = ReviewsForm
#     def form_valid(self, form):        product = get_object_or_404(Products, pk=self.kwargs.get('pk'))
#         review = form.save(commit=False)
#         review.product = product        review.author = self.request.user
#         review.save()        return redirect('webapp:article_view', pk=product.pk)
#
# class ReviewsUpdateView(PermissionRequiredMixin, UpdateView):    template_name = 'comments/comment_update.html'
#     model = Reviews    form_class = ReviewsForm
#     permission_required = 'webapp.change_comment'
#     def has_permission(self):        return super().has_permission() or self.request.user == self.get_object().author
#     def get_success_url(self):
#         return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})
# class ReviewsDeleteView(PermissionRequiredMixin, DeleteView):
#     model = Reviews    permission_required = 'webapp.delete_comment'
#     def has_permission(self):
#         return super().has_permission() or self.request.user == self.get_object().author
#     def get(self, request, *args, **kwargs):        return self.delete(request, *args, **kwargs)
#     def get_success_url(self):
#         return reverse('webapp:article_view', kwargs={'pk': self.object.product.pk})
#
