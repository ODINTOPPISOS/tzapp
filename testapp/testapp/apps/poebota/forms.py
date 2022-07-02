from django import forms
from .models import Book, Bron
from django.contrib.auth.models import User


class SearcForm(forms.Form):
    autor = forms.CharField()
    janr = forms.CharField()
    izdat = forms.CharField()

class SearcForm1(forms.Form):
    def searced(autor, janr, izdat):
        books = Book.objects.filter(book_autor=autor, book_janr=janr, book_izdat=izdat)
        print(books)
        return books


