from django.db.models.functions import Abs
from django.db.models import F, QuerySet
from book.models import BookModel

def filter_book_qs_by_loc(qs: QuerySet, loc: dict) -> QuerySet:
    return qs.annotate(
                lati_dif=Abs(F('owner__latitude') - loc.get('latitude')),
                long_dif=Abs(F('owner__longitude') - loc.get('longitude'))
            ).order_by('lati_dif', 'long_dif')
