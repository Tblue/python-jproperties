import pytest
from StringIO import StringIO
from jproperties import Properties, ParseError


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


def test_surrogate_high_without_low__garbage():
    p = Properties()

    with pytest.raises(ParseError) as excinfo:
        p.load(
            StringIO(b"surrogate=Muuusic \\ud834 foobar\n")
        )

    # Caused by garbage after the first unicode escape
    assert "High surrogate unicode escape sequence not followed by" in str(excinfo.value)


def test_surrogate_high_without_low__eof():
    p = Properties()

    with pytest.raises(ParseError) as excinfo:
        p.load(
            StringIO(b"surrogate=Muuusic \\ud834\n")
        )

    # Caused by short read (read 1 byte, wanted 6) after the first unicode escape
    assert "High surrogate unicode escape sequence not followed by" in str(excinfo.value)


def test_surrogate_high_followed_by_non_low_surrogate_uniescape():
    p = Properties()

    with pytest.raises(ParseError) as excinfo:
        p.load(
            StringIO(b"surrogate=Muuusic \\ud834\\u000a\n")
        )

    # Caused by short read (read 1 byte, wanted 6) after the first unicode escape
    assert "Low surrogate unicode escape sequence expected after high surrogate escape sequence, but got " \
           "a non-low-surrogate unicode escape sequence" in str(excinfo.value)