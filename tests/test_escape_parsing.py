# vim: fileencoding=utf-8

from jproperties import Properties
from six import BytesIO


def test_simple_escape_parsing():
    p = Properties()
    p.load(
        BytesIO(b"key value with a\\ttab\n"
                b"foo ba\\r\n"
                b"new li\\ne\n"
                b"form \\feed seen!")
    )

    assert p.properties == {"key": "value with a\ttab", "foo": "ba\r", "new": "li\ne", "form": "\feed seen!"}
