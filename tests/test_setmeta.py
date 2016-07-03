# vim: fileencoding=utf-8

import six

from jproperties import Properties


def test_setmeta_bytes():
    p = Properties()
    p["a key"] = "the value", {b"metakey": b"metaval"}

    out = six.StringIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == "#: metakey=metaval\na\\ key=the value\n"


def test_setmeta_unicode():
    p = Properties()
    p["a key"] = "the value", {u"metakey": u"ünicode metävalue!"}

    out = six.StringIO()
    p.store(out, encoding="utf-8", strip_meta=False, timestamp=False)

    out.seek(0)
    text = u"#: metakey=\\u00fcnicode met\\u00e4value\\!\na\\ key=the value\n"
    assert out.read() == text


def test_setmeta_int():
    p = Properties()
    p["a key"] = "the value", {"metakey": 42}

    out = six.StringIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == "#: metakey=42\na\\ key=the value\n"
