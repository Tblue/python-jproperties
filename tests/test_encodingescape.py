# vim: fileencoding=utf-8

import pytest
from six import BytesIO
from jproperties import Properties

@pytest.mark.parametrize("out_encoding", ["ascii", "iso-8859-1"])
def test_euro(out_encoding):
    p = Properties()

    # The euro symbol is not present in ASCII/ISO-8859-1,
    # so it should be encoded as "\u20ac".
    p["test"] = u"Euro: €"

    out = BytesIO()
    p.store(out, encoding=out_encoding, timestamp=None)

    out.seek(0)
    assert out.read() == b"test=Euro\\: \\u20ac\n"

    # Read it back again:
    out.seek(0)
    p2 = Properties()
    p2.load(out)

    assert p2.properties == {u"test": u"Euro: €"}
