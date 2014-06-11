""" A decorator for marking methods/functions as deprecated. """


# Standard library imports.
from functools import wraps
import logging
import sys
import warnings


DEPRECATION_MSG = "DEPRECATED: {module_name}, {function_name}, {message}"


def deprecated(message):
    """ A factory for decorators for marking methods/functions as deprecated.
    """

    def decorator(fn):
        """ A decorator for marking methods/functions as deprecated. """

        @wraps(fn)
        def wrapper(*args, **kw):
            """ The method/function wrapper. """
            global _cache

            module_name = fn.__module__
            function_name = fn.__name__

            if (module_name, function_name) not in _cache:
                logger = logging.getLogger(module_name)
                txt = DEPRECATION_MSG.format(module_name=module_name,
                                             function_name=function_name,
                                             message=message)
                logger.warning(txt)

                _cache.add((module_name, function_name))
                warnings.warn(message, DeprecationWarning)

            return fn(*args, **kw)

        return wrapper

    return decorator


# We only warn about each function or method once!
_cache = set()


def clear_deprecation_cache():
    """ Clear the deprecation cache.

    We clean the traits deprecation cache, which is related to *logging*, not
    warnings. We also remove each module in the cache from Python's
    ``sys.modules`` cache, which is usually enough to clear the warnings cache.
    """
    global _cache

    for module_name, function_name in _cache:
        # The same module could be present multiple times, hence the default
        # value.
        sys.modules.pop(module_name, None)
    _cache = set()

#### EOF ######################################################################
