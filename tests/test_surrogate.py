import pytest
from StringIO import StringIO
from jproperties import Properties


@pytest.mark.parametrize("out_encoding", ["ascii", "latin-1"])
def test_surrogate_roundtrip(out_encoding):
    p = Properties()
    p["surrogate"] = u"Muuusic \U0001D160"

    out = StringIO()
    p.store(out, encoding=out_encoding, timestamp=None)

    out.seek(0)
    dumped = out.read()
    assert dumped == b"surrogate=Muuusic \\ud834\\udd60\n"

    p2 = Properties()
    p2.load(dumped, out_encoding)

    assert p2["surrogate"] == (u"Muuusic \U0001D160", {})


def test_surrogate_roundtrip_utf8():
    p = Properties()
    p["surrogate"] = u"Muuusic \U0001D160"

    out = StringIO()
    p.store(out, encoding="utf-8", timestamp=None)

    out.seek(0)
    dumped = out.read()
    assert dumped == b"surrogate=Muuusic \xF0\x9D\x85\xA0\n"

    p2 = Properties()
    p2.load(dumped, "utf-8")

    assert p2["surrogate"] == (u"Muuusic \U0001D160", {})