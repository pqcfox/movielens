import numpy as np 
import collections
import csv


def load_data(fname):
    with open(fname) as f:
        reader = csv.reader(f)
        lines = list(reader)
    unique = lambda l: sorted(list(set(l)))
    movies = np.array(unique([int(line[0]) for line in lines]))
    users = np.array(unique([int(line[1]) for line in lines]))
    data = np.zeros((movies.size, users.size))
    for line in lines:
        movie, user, score = [int(value) for value in line]
        data[movies == movie, users == user] = score
    return data, movies, users 


def load_titles(fname):
    with open(fname) as f:
        reader = csv.reader(f)
        titles = [(int(id), title) for id, title in reader]
    return titles
        

def show_closest_movies(title):
    data, movies, users = load_data('largedata.csv')
    titles = load_titles('largekey.csv')
    id_to_title = {int(id): title for id, title in titles}
    title_to_id = {title: int(id) for id, title in titles}

    star_wars_id = title_to_id[title]
    star_wars = data[movies == star_wars_id, :]
    norms = np.linalg.norm(data - star_wars, axis=1)
    index_order = np.argsort(norms)[1:]
    movie_order = movies[index_order]
    norm_order = norms[index_order]

    print('Closest movies to {}:'.format(title))
    for i, (movie, norm) in enumerate(zip(movie_order, norm_order)):
        title = id_to_title[movie]
        print('{}: {} ({})'.format(i + 1, title, norm))

title = input('Enter movie title: ')
show_closest_movies(title)

