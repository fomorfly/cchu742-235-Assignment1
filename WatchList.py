# Chong Sheng Chuah
# cchu742
# 910742929
# ===================================================
# Assignment 1 WatchList implementation


class WatchList:

    def __init__(self):
        self.__movies = []  # a list of Movie() representing a watchlist (queue)

    @property
    def movies(self):
        return self.__movies

    # add movie to watchlist if the movie is not already in watchlist
    def add_movie(self, movie):
        if movie not in self.__movies:
            self.__movies.append(movie)

    # remove a movie, if the movie is not in watchlist, do nothing
    def remove_movie(self, movie):
        if movie in self.__movies:
            self.__movies.remove(movie)

    # takes in an index and returns the movie at the index, returns None if index out of range
    def select_movie_to_watch(self, index):
        if index <= len(self.__movies) - 1:
            return self.__movies[index]
        return None

    # returns the size of the watchlist
    def size(self):
        return len(self.__movies)

    # returns the first movie in watchlist (first in queue)
    def first_movie_in_watchlist(self):
        if len(self.__movies) > 0:
            return self.__movies[0]
        else:
            return None

    def __iter__(self):
        self.__i = -1
        return self

    def __next__(self):
        self.__i = self.__i + 1
        if self.__i <= len(self.__movies)-1:
            return self.__movies[self.__i]
        else:
            raise StopIteration
