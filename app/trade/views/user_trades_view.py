from django.db.models.query import QuerySet
from django.views.generic import  ListView
from ..models import TradeModel
from django.contrib.auth.mixins import LoginRequiredMixin

class UserRequestsView(LoginRequiredMixin, ListView):
    """ show all user requests  """
    model = TradeModel
    template_name = 'trade/user_requests.html'
    context_object_name = 'trades'

    def get_queryset(self):
        return TradeModel.objects.filter(                                                               
            user=self.request.user
        ).select_related('book', 'user').all().order_by('-created_at')

