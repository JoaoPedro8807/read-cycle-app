from django.shortcuts import render
from django.urls import reverse_lazy
from ..models import BookModel, AvaliationModel
from ..forms import AvaliationForm
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class AvaliationView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        book = get_object_or_404(BookModel, pk=kwargs['pk'])
        if AvaliationModel.objects.filter(
            user=request.user,
            post=book
        ).exists():
            return render(request, 'book/book_message.html', context={
                'messages': ['Você já avaliou esse livro']
            })
        
        form = AvaliationForm(data=request.POST)
        if form.is_valid(): 
            AvaliationModel.objects.create(
                post=book,
                user=request.user,
                body=form.cleaned_data['body'],
                title=form.cleaned_data['title'],
                rating=form.cleaned_data['rating']
            )
            return render(request, 'book/book_message.html', context={
                'messages': ['Avalição criada com sucesso']
            })
         
    
    