from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    if not movie_repository.get_all_movies:
        return render_template('list_all_movies.html', list_movies_active=False)
    else:
      
        return render_template('list_all_movies.html', list_movies_active=True, repo = movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    theTitle = request.form['title']
    theDirector = request.form['director']
    theRating = request.form['rating']

    movie_repository.create_movie(str(theTitle), str(theDirector), int(theRating))
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    
    search = request.args.get('title')
    print(str(search))
    if(search == None):
        return render_template('search_movies.html', search_active=False)
    else:
        return render_template('search_movies.html', search_active=True, movie = movie_repository.get_movie_by_title(search))
