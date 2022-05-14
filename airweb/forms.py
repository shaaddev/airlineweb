
from django import forms
from .models import Book, Contact

# Create Forms here

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email_address', 'first_name', 'last_name', 'country')


    