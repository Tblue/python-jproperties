from io import BytesIO
from jproperties import Properties

def test_basic_equals_sign():
    p = Properties()
    p.load("Truth = Beauty\n")
    assert p.properties == {"Truth": "Beauty"}

def test_basic_colon_and_leading_whitespace():
    p = Properties()
    p.load("  Truth:Beauty")
    assert p.properties == {"Truth": "Beauty"}

def test_basic_key_trailing_space():
    p = Properties()
    p.load("Truth                    :Beauty")
    assert p.properties == {"Truth": "Beauty"}

def test_basic_whitespace():
    p = Properties()
    p.load('''fruits            apple, banana, pear, \\
                                cantaloupe, watermelon, \\
                                kiwi, mango''')

    assert p.properties == {'fruits': 'apple, banana, pear, cantaloupe, '
                                      'watermelon, kiwi, mango'}

def test_basic_key_only():
    p = Properties()
    p.load('cheese\n')

    assert p.properties == {'cheese': ''}

def test_basic_escape_write():
    p = Properties()
    p['key'] = 'hello\nworld'

    out = BytesIO()
    p.store(out, timestamp=None)

    out.seek(0)
    assert out.read() == b'key=hello\\nworld\n'
