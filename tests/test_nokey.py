from jproperties import Properties

def test_nokey():
    p = Properties()
    p.load("= no key!")

    assert p.properties == {"": "no key!"}
    assert p[""] == ("no key!", {})

def test_nokey_repeated():
    p = Properties()
    p.load("= no key!\n: still no key!")

    assert p.properties == {"": "still no key!"}
    assert p[""] == ("still no key!", {})
