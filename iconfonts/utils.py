# -*- coding: utf-8 -*-
import re
import sys
from xml.etree.ElementTree import _escape_attrib_html

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
    unicode = str
else:
    string_types = unicode, str

string = string_types[0]
iterable_types = list, set

escape = lambda value, encoding='utf-8': _escape_attrib_html(value, encoding)
key_pattern = re.compile('[a-zA-Z_:][-a-zA-Z0-9_:.]*')


class RegisterLeafClasses(type):
    """
    Self-Registration of Subclasses.
    http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Metaprogramming.html#example-self-registration-of-subclasses
    """
    def __init__(cls, name, bases, nmspc):
        super(RegisterLeafClasses, cls).__init__(name, bases, nmspc)
        if not hasattr(cls, 'registry'):
            cls.registry = set()
        cls.registry.add(cls)
        cls.registry -= set(bases) # Remove base classes
    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.registry)
    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])


def check_key(key):
    if not key_pattern.match(key):
        raise AttributeError("Invalid key '%s'" % key)
    return key

def flatatt(attributes, encoding='utf-8'):
    return string('').join([
        string(' {0}="{1}"').format(check_key(key), escape(val, encoding))
        for key, val in sorted(attributes.items())
    ])