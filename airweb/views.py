from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Book, Contact
from .forms import BookForm, ContactForm

# Create your views here.
class HomePage(TemplateView):
    template_name = 'airline/index.html'

class BookPage(CreateView):
    form_class = BookForm
    template_name = 'airline/book.html'
    success_url = reverse_lazy('thanks')

class AboutPage(TemplateView):
    template_name = 'airline/about.html'

class ContactPage(CreateView):
    form_class = ContactForm
    template_name = 'airline/contact.html'
    success_url = reverse_lazy('congrats')

class Thanks(TemplateView):
    template_name = 'thanks/thanks.html'

class Congrats(TemplateView):
    template_name = 'thanks/congrats.html'