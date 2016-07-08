from jproperties import Properties

def test_novalue():
    p = Properties()
    p.load(br"no\ value!")

    assert p.properties == {"no value!": ""}
