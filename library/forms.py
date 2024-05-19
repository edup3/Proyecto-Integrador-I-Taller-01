
from django import forms
from .models import Book

class LibroForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image', 'reserved_date', 'reserved']
