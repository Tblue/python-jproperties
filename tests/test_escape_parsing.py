# vim: fileencoding=utf-8

from jproperties import Properties
from StringIO import StringIO


def test_simple_escape_parsing():
    p = Properties()
    p.load(
        StringIO("key value with a\\ttab\n"
                 "foo ba\\r\n"
                 "new li\\ne\n"
                 "form \\feed seen!")
    )

    assert p.properties == {"key": "value with a\ttab", "foo": "ba\r", "new": "li\ne", "form": "\feed seen!"}