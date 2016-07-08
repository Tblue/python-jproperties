# vim: fileencoding=utf-8

from jproperties import Properties
from StringIO import StringIO


def test_line_contination_allowed():
    p = Properties()
    p.load(
        StringIO(r"""
            multi\
            line\ key = value
        """)
    )

    assert p.properties == {"multiline key": "value"}

def test_line_contination_forbidden():
    # In metadata comments, line continuation is disabled.

    p = Properties()
    p.load(
        StringIO(r"""
            #: metakey meta\
            value continuation

            multi\
            line\ key = value
        """)
    )

    assert p.properties == {"multiline key": "value", "value": "continuation"}