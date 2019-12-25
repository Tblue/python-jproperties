from jproperties import Properties

def test_skip_docstr():
    p = Properties()
    p.load("# A comment\nK = V\n# More comments\n")
    assert p.properties == {"K": "V"}
    assert p.getmeta("K") == {}

def test_simple_docstr():
    p = Properties()
    p.load("#\nK = V\n# A comment\n", metadoc=True)
    assert p.properties == {"K": "V"}
    assert p.getmeta("K") == {"_doc": "A comment\n"}

def test_simple_docstr_without_eol():
    p = Properties()
    p.load("#\nK = V\n# A comment", metadoc=True)
    assert p.properties == {"K": "V"}
    assert p.getmeta("K") == {"_doc": "A comment\n"}

def test_simple_docstr_w_meta():
    p = Properties()
    p.load("#: metakey=42\nK = V\n# A comment\n", metadoc=True)
    assert p.properties == {"K": "V"}
    assert p.getmeta("K") == {"_doc": "A comment\n", "metakey": '42'}

def test_multiline_docstr():
    p = Properties()
    p.load("#\nK = V\n# A comment\n#   more comments\n", metadoc=True)
    assert p.properties == {"K": "V"}
    assert p.getmeta("K") == {"_doc": "A comment\n  more comments\n"}

def test_multiline_docstr_without_eol():
    p = Properties()
    p.load("#\nK = V\n# A comment\n#   more comments", metadoc=True)
    assert p.properties == {"K": "V"}
    assert p.getmeta("K") == {"_doc": "A comment\n  more comments\n"}

def test_multiline_docstr_with_empty_lines():
    p = Properties()
    p.load("K = V\n# A comment\n#   more comments\n\n\n# trailer\n", metadoc=True)
    assert p.properties == {"K": "V"}
    assert p.getmeta("K") == {"_doc": "A comment\n  more comments\ntrailer\n"}
