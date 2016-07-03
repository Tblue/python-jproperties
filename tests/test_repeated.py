from jproperties import Properties

def test_repeated():
    p = Properties()
    p.load(b"key:value\nkey=the value\nkey = value1\nkey : value2\nkey value3\nkey\tvalue4")

    assert p.properties == {"key": "value4"}


def test_repeated_with_meta():
    p = Properties()
    p.load(b"""
        key = value1

        #: metakey = metaval1
        #: metakey2 = metaval22
        key = value2

        # Expected: Metadata should ONLY contain the following
        # 'metakey' key.
        #: metakey = metaval2
        key = value3
    """)

    assert p.properties == {"key": "value3"}
    assert p["key"] == ("value3", {"metakey": "metaval2"})
