# vim: fileencoding=utf-8

from jproperties import Properties
from six import BytesIO


def test_line_continuation_allowed():
    p = Properties()
    p.load(
        BytesIO(br"""
            multi\
            line\ key = value
        """)
    )

    assert p.properties == {"multiline key": "value"}


def test_line_continuation_forbidden():
    # In metadata comments, line continuation is disabled.

    p = Properties()
    p.load(
        BytesIO(br"""
            #: metakey meta\
            value continuation

            multi\
            line\ key = value
        """)
    )

    assert p.properties == {"multiline key": "value", "value": "continuation"}


def test_stray_line_continuation():
    p = Properties()
    p.load(
        BytesIO(b"key value\\")
    )

    assert p.properties == {"key": "value"}
