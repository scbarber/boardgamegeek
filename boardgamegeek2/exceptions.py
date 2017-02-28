# coding: utf-8
"""
:mod:`boardgamegeek2.exceptions` - Exceptions
============================================

.. module:: boardgamegeek2.exceptions
   :platform: Unix, Windows
   :synopsis: exceptions used in the package

.. moduleauthor:: Cosmin Luță <q4break@gmail.com>
"""


class BGGValueError(ValueError):
    """ invalid parameters """
    pass


class BGGError(Exception):
    """ Base class for errors """
    pass


class BGGItemNotFoundError(BGGError):
    """ Requested item was not found """
    pass


class BGGApiTimeoutError(BGGError):
    """ Network timeout issues """
    pass


class BGGApiError(BGGError):
    """ An error related to the BGG XML2 API """
    pass


class BGGApiRetryError(BGGApiError):
    """ The request to the BGG XML2 API should be retried """
    pass

