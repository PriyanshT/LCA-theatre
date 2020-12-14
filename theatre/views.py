from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import Movie
from .models import Coin
from .models import UserMovie
from .forms import CreateUserForm

from django.contrib import messages


def index(request):
    return render(request, 'theatre/index.html')


def allMovies(request):
    user = request.user
    allMovies = Movie.objects.all()
    try:
        userMovies = UserMovie.objects.all().filter(user=user.username)
        context = {
            'my_movies': userMovies,
            'all_movies': allMovies
        }

    except:
        context = {
            'all_movies': allMovies
        }

    return render(request, 'theatre/allMovies.html', context)


def myMovies(request):
    user = request.user
    try:
        movies = UserMovie.objects.all().filter(user=user.username)
        context = {
            'my_movies': movies
        }

    except:
        context = {}

    return render(request, 'theatre/myMovies.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('theatre:index')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                coin_instance = Coin.objects.create(user=user, spare_coin='20')
                messages.success(request, 'Account was created for ' + user)

                return redirect('theatre:login')

    context = {'form': form}
    return render(request, 'theatre/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('theatre:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('theatre:index')
            else:
                messages.info(request, 'Username or Password is Incorrect!')

    context = {}
    return render(request, 'theatre/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('theatre:index')


def movieView(request, clip):
    user = request.user
    loggedUserMovies = UserMovie.objects.all().filter(user=user.username)
    # To check if the user is authorized to watch the movie
    for singleMovie in loggedUserMovies:
        if singleMovie.movie.clip == clip:
            movie = get_object_or_404(Movie, clip=clip)
            return render(request, 'theatre/movieView.html', {'movie': movie})
    # Unauthorized access
    return redirect('theatre:index')


def checkAvailability(request, movieTitle):
    user = request.user
    loggedUserMovies = UserMovie.objects.all().filter(user=user.username)
    movie = Movie.objects.filter(movie_title=movieTitle).first()
    # To check if the user has already bought the movie
    for singleMovie in loggedUserMovies:
        if singleMovie.movie.movie_title == movieTitle:
            context = {
                'movie': movie
            }
            return render(request, 'theatre/checkAvailability.html', context)
    context = {
        'movie': movie,
        'notAvail': 1
    }
    return render(request, 'theatre/checkAvailability.html', context)


def buyMovie(request, movieTitle):
    movie = Movie.objects.filter(movie_title=movieTitle).first()
    if request.user.is_authenticated:
        user = request.user
        loggedUserMovies = UserMovie.objects.all().filter(user=user.username)
        # To check if the user has already bought the movie
        for singleMovie in loggedUserMovies:
            if singleMovie.movie.movie_title == movieTitle:
                context = {
                    'movie': movie
                }
                return render(request, 'theatre/checkAvailability.html', context)
        # To check if the user has enough spare coins
        spareCoin = Coin.objects.filter(user=user.username).first()
        if spareCoin.spare_coin < movie.price:
            messages.error(request, 'Not enough spare Coins!')
            context = {
                'movie': movie,
                'notAvail': 1
            }
            return render(request, 'theatre/checkAvailability.html', context)
        # Buy Movie and deduct Spare Coins
        else:
            # Deduct Coins of user
            spareCoin.spare_coin -= movie.price
            newSpareCoin = Coin.objects.filter(
                user=user.username).update(spare_coin=spareCoin.spare_coin)
            # Add movie to user table
            addMovie = UserMovie.objects.create(
                user=user.username, movie=movie)
            addMovie.save()
            messages.success(request, 'Movie Bought for ' + user.username)
            context = {
                'movie': movie
            }
            return render(request, 'theatre/checkAvailability.html', context)
    else:
        messages.success(request, 'Login to continue buying movies.')
        context = {
            'movie': movie,
            'notAvail': 1
        }
        return render(request, 'theatre/checkAvailability.html', context)
