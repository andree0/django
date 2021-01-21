from .models import Movie, PersonMovie, Person
from .forms import PersonForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.


def base_html(request):
    """Strona główna aplikacji Filmwebapp"""
    return render(request, "base.html")


def start_html(request):
    start_web = '''<h2>myFilmweb</h2><br><br>
    <p><a href=http://127.0.0.1:8000/movies/>Baza filmów</a></p>
    <p><a href=http://127.0.0.1:8000/persons/>Baza osób</a></p>'''
    return HttpResponse(start_web)


def movies(request):
    movies_list = Movie.objects.all().order_by('-year')
    context = {'movies': movies_list}
    return render(request, "movies.html", context)


def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    genres = []
    actors = []
    for genre in movie.genre.values_list('name'):
        genres.append(genre[0])
    for starring in PersonMovie.objects.filter(movie=movie_id).values_list('person', 'role'):
        actors.append((Person.objects.get(pk=starring[0]), starring[1]))
    genres = ' / '.join(genres)
    context = {'movie': movie,
               'genres': genres,
               'actors': actors
               }
    return render(request, "movie_details.html", context)


# def edit_movie(request, movie_id):
#     movie_edit = get_object_or_404(Movie, pk=movie_id)
#     if request.method == 'POST':
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             movie_edit.first_name = form.cleaned_data['first_name']
#             movie_edit.last_name = form.cleaned_data['last_name']
#             movie_edit.save()
#             return movies(request)
#     else:
#         form = MovieForm()
#         context = {'form': form}
#         return render(request, 'edit_movie.html', context)


def persons(request):
    persons_list = Person.objects.all()
    context = {'persons': persons_list}
    return render(request, 'persons.html', context)


def edit_person(request, person_id):
    person_edit = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person_edit)
        if form.is_valid():
            form.save(commit=False)
            # person_edit.first_name = form.cleaned_data['first_name']
            # person_edit.last_name = form.cleaned_data['last_name']
            form.save()
            return persons(request)
    else:
        form = PersonForm(instance=person_edit)
        context = {'form': form}
        return render(request, 'edit_person.html', context)

# def edit_person(request, person_id):
#     person = Person.objects.get(pk=person_id)
#     if request.method == 'GET':
#         context = {'person': person}
#         return render(request, 'edit-person.html', context)
#     elif request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         person.first_name = first_name
#         person.last_name = last_name
#         person.save()
#         return persons(request)


def add_person(request):
    if request.method == 'GET':
        form = PersonForm()
        context = {'form': form}
        return render(request, 'add_person.html', context)
    elif request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            new_person = Person(first_name=first_name, last_name=last_name)
            new_person.save()
            return persons(request)