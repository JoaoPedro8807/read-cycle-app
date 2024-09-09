from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..models import BookModel
from ..forms import CreateBookForm
from django.views import View
from ..services import fetch_volume_data, download_image
from ..forms import EntryBookDataForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class BookView(View):
    """ show the initial form, fetch data in api, merge above data and send to confirmation view """
    def get(self, request, *args, **kwargs):
        form = EntryBookDataForm()
        return render(
            request,
            'book/create_book.html',
            context={
                'form':  form
            }
        )
    
    def post(self, request, *args, **kwargs):
        print('TESTE')
        form = EntryBookDataForm(request.POST, request.FILES)
        if form.is_valid():                                                         
            title = form.cleaned_data['title']
            authors = form.cleaned_data['authors']

            api_data = fetch_volume_data(title=title, authors=[authors]) #fetch in google api
            print('DATA_API: ', api_data)
            request.session['volume_data'] = api_data 
            book_form = CreateBookForm(data=api_data) 

            context={
                'form': book_form,
                'api_image': api_data.get('image', None)
            }
        else:
            context={
                'message': form.errors
            }
        return render(
            request,
            'book/confirm_create_book.html',
            context=context
           
        )

class ConfirmCreateBookView(LoginRequiredMixin, CreateView): 
    """ confirm and save the final book data """
    form_class = CreateBookForm
    template_name = 'book/create_book1.html'
    success_url = reverse_lazy('book:my-list-book-page')
    
    #get the volume data from session, merge and update form.
    def form_valid(self, form): 
        volume_data = self.request.session.pop('volume_data', {}) 
        print('VOLUME DATA: ', volume_data)
        title = form.cleaned_data['title']

        if BookModel.objects.filter(
            title=title, 
            owner=self.request.user,
            book_api_id=volume_data.get('book_api_id', '')
            ).exists():
            form.add_error('title', 'Você já cadastrou esse livro.')
            return self.form_invalid(form)
        
        form.instance.owner = self.request.user
        if not form.cleaned_data['image']:
            form.cleaned_data.pop('image') 

        merge_data = {**volume_data, **form.cleaned_data} 
        print('merge data: ', merge_data)

        image_content = form.cleaned_data.get('image') or download_image(merge_data.get('image'))
        form.instance.image.save('', image_content, save=False) #model will save in the correct path

        for key, value in merge_data.items():
            form.cleaned_data[key] = value
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
    
        messages.error(self.request, message=form.errors)
        return redirect('book:book-create-page')    
    