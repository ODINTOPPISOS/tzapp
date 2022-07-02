from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Book, Bron

admin.site.register(Book)
admin.site.register(Bron)

"""if user is not None:
    print("lab")
else:
    print("net")
    admin.site.register(Book)
    admin.site.register(Bron)

adm = authenticate(username='admin', password='123')
if adm is not None:
    print("adm")

else:
    print("net")
"""