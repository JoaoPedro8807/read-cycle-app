from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import DeleteView
from ..models import BookModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

@login_required
def delete_book_view(request, pk):
    book = get_object_or_404(
        BookModel.objects.all().select_related(
        'owner')
        .prefetch_related('category'),
        pk=pk,
        owner=request.user
    )
    book.delete()
    new_list = BookModel.objects.all().filter(
        owner=request.user
    )


    return render(
        request,
        'book/render_book_list.html',
        context={
            'object_list': new_list
        }
    )

