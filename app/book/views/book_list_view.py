from typing import Any
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.views.generic import ListView
from ..models import BookModel
from django.core.paginator import Paginator
from django.conf import settings
from ..filters.book_home_page_filter import BookHomeFilter
import json
from ..services import filter_book_qs_by_loc
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(ListView):
    model = BookModel
    template_name = 'book/all_book_list_template.html'
    paginate_by = settings.NUMBER_PAGINATION_LIST

    def get_queryset(self):
        return BookModel.objects.books_available().select_related(
            'owner', 'category').order_by('-created_at')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        query_filter = BookHomeFilter(self.request.GET, self.get_queryset())
        
        qs = query_filter.qs
        user_locale =  self.request.GET.get('proximidade')

        if user_locale:
            qs = filter_book_qs_by_loc(
                qs=query_filter.qs,
                loc=json.loads(user_locale)
            )
        page = self.request.GET.get('page', 1)  
        paginator = Paginator(qs, self.paginate_by)

        books = paginator.page(page)

        context['object_list'] = books
        context['filter_form'] = query_filter
        return  context

    def get_template_names(self) -> list[str]:
        if self.request.headers.get('partial'):
            return 'book/render_book.html' #return nexts books to inifite scroll page
        
        return 'book/all_book_list_template.html'


class MyBooksListView(LoginRequiredMixin, ListView):
    """ show the user books """
    model = BookModel
    template_name = 'book/user_book_list.html'


    def get_queryset(self):
        return  BookModel.objects.filter(
            owner=self.request.user
        )

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        qs = self.get_queryset()
        context['total_user_books_available'] = qs.filter(available=True).count()
        context['total_user_books_unavailable'] = int(context['object_list'].count()  - context['total_user_books_available'])
        return context
    






    
    
    

    
