# vim: fileencoding=utf-8

import six

from jproperties import Properties

def test_setmeta_bytes():
    p = Properties()
    p["a key"] = "the value", {b"metakey": b"metaval"}

    # out = six.StringIO()
    out = six.BytesIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == b"#: metakey=metaval\na\\ key=the value\n"

def test_setmeta_unicode():
    p = Properties()
    p["a key"] = "the value", {u"metakey": u"Ã¼nicode metÃ¤value!"}

    # out = six.StringIO()
    out = six.BytesIO()
    p.store(out, encoding="utf-8", strip_meta=False, timestamp=False)

    out.seek(0)
    text = u"#: metakey=Ã¼nicode metÃ¤value\\!\na\\ key=the value\n"
    assert out.read() == text.encode('utf-8')

def test_setmeta_int():
    p = Properties()
    p["a key"] = "the value", {"metakey": 42}

    # out = six.StringIO()
    out = six.BytesIO()
    p.store(out, strip_meta=False, timestamp=False)

    out.seek(0)
    assert out.read() == b"#: metakey=42\na\\ key=the value\n"
