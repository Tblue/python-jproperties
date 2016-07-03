# vim: fileencoding=utf-8

from jproperties import Properties
from six import StringIO

def test_setmeta_bytes():
    p = Properties()
    p["a key"] = "the value", {b"metakey": b"metaval"}

    out = StringIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == "#: metakey=metaval\na\\ key=the value\n"

def test_setmeta_unicode():
    p = Properties()
    p["a key"] = "the value", {u"metakey": u"ünicode metävalue!"}

    out = StringIO()
    p.store(out, encoding="utf-8", strip_meta=False, timestamp=False)

    out.seek(0)
    text = "#: metakey=ünicode metävalue\\!\na\\ key=the value\n"
    assert out.read() == text

def test_setmeta_int():
    p = Properties()
    p["a key"] = "the value", {"metakey": 42}

    out = StringIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == "#: metakey=42\na\\ key=the value\n"
