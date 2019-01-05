#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "bomazani"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    raise NotImplementedError("Complete this decorator function")


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        if len(src) != 0:
            return f.read().splitlines()
        else:
            return


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))

# print(timeit.timeit('''def main():
#     result = find_duplicate_movies('movies.txt')
#     print('Found {} duplicate movies:'.format(len(result)))
#     print('\n'.join(result))''', number = 100))


if __name__ == '__main__':
    import timeit
    times = (timeit.repeat(
        "main()", setup="from __main__ import main", repeat=3, number=3))
    print(times)
    print('Shortest avg runtime is {}.'.format(min(times)/3))
