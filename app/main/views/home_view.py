from typing import Any
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, View
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from book.models import BookModel
from django.http.response import HttpResponse
import json
from django.db.models import F
from django.db.models.functions import Abs

class BookHomeView(View):

    def get_queryset(self, max: int = None):
        return BookModel.objects.all_books()[:max] #lazy
         
    def get(self, request, *args, **kwargs):
        qs = self.get_queryset(9)
        print('QS: ', qs)
        return render(
            request=request,
            template_name='main/home.html',
            context={
                'recomended_books': qs
            })

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        lati = data.get('latitude')
        long = data.get('longitude')

        qs = self.get_queryset()
        recomend_book = qs.annotate(
            lati_dif=Abs(F('owner__latitude') - lati),
            long_dif=Abs(F('owner__longitude') - long)
        ).order_by('lati_dif', 'long_dif')[:9]

        return render(
            request=request,
            template_name='main/render_book_card.html',
            context={
                'recomended_books': recomend_book
        })


        

