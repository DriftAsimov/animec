# -*- coding: utf-8 -*-

class NoResultFound(Exception):
    """Raised if no result is found or there is a HTTP error"""  
    
    pass

class TooManyRequests(Exception):
    """Raised when number of requests exceed than the expected"""
    pass
