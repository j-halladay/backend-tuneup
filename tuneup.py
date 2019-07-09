#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import functools
import timeit
# import StringIO


def profile(func):
    @functools.wraps(func)
    def innertimer(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        func(*args, **kwargs)
        pr.disable()

        ps = pstats.Stats(pr).sort_stats("cumulative")
        ps.print_stats()

        return func(*args, **kwargs)
    return innertimer
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    raise NotImplementedError("Complete this decorator function")


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie == title:
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    setup = """
import tuneup
result = tuneup.find_duplicate_movies('movies.txt')
    """
    f = min(timeit.Timer("result", setup=setup).repeat(
        repeat=7, number=3))
    formated = format(f, ".10f")
    print("Best time across 7 repeats of 5 runs per repeat: {} sec".format(formated))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')

    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    # timeit_helper()


if __name__ == '__main__':
    main()
