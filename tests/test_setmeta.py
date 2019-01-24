# vim: fileencoding=utf-8

from jproperties import Properties
from six import BytesIO

def test_setmeta_bytes():
    p = Properties()
    p["a key"] = "the value", {b"metakey": b"metaval", b"__internal": b"foo"}

    out = BytesIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == b"#: metakey=metaval\na\\ key=the value\n"

def test_setmeta_unicode():
    p = Properties()
    p["a key"] = "the value", {u"metakey": u"ünicode metävalue!", u"__internal": u"foo"}

    out = BytesIO()
    p.store(out, encoding="utf-8", strip_meta=False, timestamp=False)

    out.seek(0)
    text = u"#: metakey=ünicode metävalue\\!\na\\ key=the value\n".encode("utf-8")
    assert out.read() == text

def test_setmeta_int():
    p = Properties()
    p["a key"] = "the value", {"metakey": 42}

    out = BytesIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == b"#: metakey=42\na\\ key=the value\n"
