
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
