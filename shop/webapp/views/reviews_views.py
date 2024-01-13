from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from webapp.models import Product, Review
from webapp.forms import ReviewForm
from django.urls import reverse_lazy


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_view.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(is_moderated=True)


class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product = get_object_or_404(Product, id=self.kwargs['product_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.kwargs['product_id']})


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_update.html'

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.id})


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.id})
