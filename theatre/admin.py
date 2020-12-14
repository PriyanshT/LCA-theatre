from django.contrib import admin
from .models import Movie
from .models import Coin
from .models import UserMovie

admin.site.register(Movie)
admin.site.register(Coin)
admin.site.register(UserMovie)
