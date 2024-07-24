# vim: fileencoding=utf-8

from six import BytesIO

from jproperties import Properties


def test_pretty_print_simple():
    p = Properties()

    p["test"] = "Hello\r\nWorld!\ntrailer\rend"

    out = BytesIO()
    p.store(out, timestamp=None, encoding="utf-8", pretty_print=True)

    out.seek(0)
    assert out.read() == b"""\
test=Hello\\r\\n\\
    World\\!\\n\\
    trailer\\r\\
    end
"""

    # Read it back again:
    out.seek(0)
    p2 = Properties()
    p2.load(out)

    assert p2.properties == {"test": "Hello\r\nWorld!\ntrailer\rend"}

def test_pretty_print_trailing_newline():
    p = Properties()

    p["test"] = "Hello\nWorld!\n"
    p["test2"] = "Moo"

    out = BytesIO()
    p.store(out, timestamp=None, encoding="utf-8", pretty_print=True)

    out.seek(0)
    assert out.read() == b"""\
test=Hello\\n\\
    World\\!\\n\\
    
test2=Moo
"""

    # Read it back again:
    out.seek(0)
    p2 = Properties()
    p2.load(out)

    assert p2.properties == {"test": "Hello\nWorld!\n", "test2": "Moo"}

def test_pretty_print_trailing_newline_eof():
    p = Properties()

    p["test"] = "Hello\nWorld!\n"

    out = BytesIO()
    p.store(out, timestamp=None, encoding="utf-8", pretty_print=True)

    out.seek(0)
    assert out.read() == b"""\
test=Hello\\n\\
    World\\!\\n\\
    
"""

    # Read it back again:
    out.seek(0)
    p2 = Properties()
    p2.load(out)

    assert p2.properties == {"test": "Hello\nWorld!\n"}

def test_pretty_print_simple_in_strict_mode():
    p = Properties()

    p["test"] = "Hello\nWorld!"

    # We write this out in the (default) strict mode with the (default) iso-8859-1
    # encoding, and that means that pretty_print should be ignored:
    out = BytesIO()
    p.store(out, timestamp=None, pretty_print=True)

    out.seek(0)
    assert out.read() == b"""\
test=Hello\\nWorld\\!
"""

    # Read it back again:
    out.seek(0)
    p2 = Properties()
    p2.load(out)

    assert p2.properties == {"test": "Hello\nWorld!"}
