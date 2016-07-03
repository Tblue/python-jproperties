import pytest
from jproperties import Properties, InterpolationError


def test_interpolation_simple():
    p = Properties()
    p.load('first = asdf\nsecond = start ${first} stop\n')

    assert p.properties == {'first': 'asdf', 'second': 'start asdf stop'}


def test_interpolation_disabled():
    p = Properties(use_interpolation=False)
    p.load('first = asdf\nsecond = start ${first} stop\n')

    assert p.properties == {'first': 'asdf', 'second': 'start ${first} stop'}


def test_interpolation_nested():
    p = Properties()
    p.load('first = asdf\nsecond = ${first}\nthird = ${second}\n')

    assert p.properties == {'first': 'asdf', 'second': 'asdf', 'third': 'asdf'}


def test_interpolation_tree():
    p = Properties()
    p.load("root = i'm a tree\na = ${root}\nb = ${root}\nc = ${root}\n")

    assert p.properties == {'root': "i'm a tree", 'a': "i'm a tree",
                            'b': "i'm a tree", 'c': "i'm a tree"}


def test_interpolation_error_missing():
    p = Properties()
    with pytest.raises(InterpolationError) as excinfo:
        p.load('first = asdf\nsecond = here ${missing} there\n')

    assert issubclass(excinfo.type, InterpolationError)


def test_interpolation_error_circular():
    p = Properties()
    with pytest.raises(InterpolationError) as excinfo:
        p.load('first = this ${second} that\nsecond = here ${first} there\n')

    assert issubclass(excinfo.type, InterpolationError)

