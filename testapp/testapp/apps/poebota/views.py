from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from .models import Book, Bron
from .forms import SearcForm, SearcForm1
from django.utils import timezone
from datetime import timedelta
# Создаём логику приложения
def index(request):

    if request.method == "POST":
        autor = request.POST.get("autor")
        janr = request.POST.get("janr")
        izdat = request.POST.get("izdat")
        books = Book.objects.filter(book_autor=autor, book_janr=janr, book_izdat=izdat)
        bron = Bron.objects.all()
        return render(request, "home/search.html", {'books': books, 'bron': bron})
    else:
        books = Book.objects.all()
        bron = Bron.objects.all()
        userform = SearcForm()
        return render(request, "index.html", {"form": userform, 'books': books, 'bron': bron})

def create(request, book_id):
    if request.method == "POST":
        bron_create = Bron.objects.get(id=book_id)
        if bron_create.bron_status == "Да" and bron_create.bron_login == request.POST.get("login") and bron_create.bron_password == request.POST.get("password"):
            bron_create.bron_status = "Нет"
            bron_create.bron_time = timezone.now()
            bron_create.bron_login = ""
            bron_create.bron_password = ""
            bron_create.save()
            print("бронь снята")
        elif bron_create.bron_status == "Нет":
            if request.user.is_authenticated == True:
                bron_create.bron_status = "Да"
                bron_create.bron_time = timezone.now() + timedelta(days=7)
                bron_create.bron_login = str(request.user)
                bron_create.bron_password = request.POST.get("password")
                bron_create.save()
                print("бронь установлена")
        else:
            raise Http404("Не верный логин или пароль")
    try:
        book = Book.objects.get(id=book_id)
        bron = Bron.objects.get(id=book_id)
    except:
        raise Http404("Книга не найдена")
    return render(request, 'home/create.html', {'book': book, 'bron': bron})


def get_data(request):
    return render(request, "home/home.html")

