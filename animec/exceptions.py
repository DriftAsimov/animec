# This file contains all the exceptions for the module.

class NotFound404(Exception):
    """This exception is raised when No Result is Found for Anime class"""
    pass

class NoResultFound(Exception):
    """ This exception is raised if no result is found for CharSearch class and AniLyrics class"""
    pass

class TooManyRequests(Exception):
    """This exception is raised when the number of requests is very high for Aninews class"""
    pass
