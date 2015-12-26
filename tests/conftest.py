# "datadir" fixture for pytest.
#
# Copyright (c) 2015, Tilman Blumenbach
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import pytest


class _Datadir(object):
    def __init__(self, request):
        basedir = request.fspath.dirpath()
        testdir = basedir.join(request.module.__name__)

        self._datadirs = [testdir, basedir.join("data")]

        if request.cls is not None:
            clsdir = testdir.join(request.cls.__name__)
            self._datadirs[:0] = [clsdir.join(request.function.__name__), clsdir]
        else:
            self._datadirs.insert(0, testdir.join(request.function.__name__))

    def __getitem__(self, path):
        for datadir in self._datadirs:
            datadir_path = datadir.join(path)
            if datadir_path.check():
                return datadir_path

        raise KeyError("File `%s' not found in any of the following datadirs: %s" % (path, self._datadirs))

@pytest.fixture
def datadir(request):
    """
    Provides a "datadir" fixture which allows test functions to
    easily access resources in data directories. It was inspired
    by the `pytest-datadir plugin
    <https://github.com/gabrielcnr/pytest-datadir>`_.

    The "datadir" fixture behaves like a dictionary. Currently,
    only retrieving items using the ``d[key]`` syntax is supported.
    Things like iterators, ``len(d)`` etc. are not.

    How the fixture looks for resources is best described by an example.
    Let us assume the following directory structure for your tests:

    .. code-block:: none

        tests/
        +-- test_one.py
        +-- test_two.py
        +-- data/
        |   +-- global.dat
        +-- test_one/
        |   +-- test_func/
        |       +-- data.txt
        +-- test_two/
            +-- TestClass/
                +-- test_method/
                    +-- strings.prop

    The file ``test_one.py`` contains the following function::

        def test_func(datadir):
            data_path = datadir["data.txt"]

            # ...

    The file ``test_two.py`` contains the following class::

        class TestClass(object):
            def test_method(self, datadir):
                strings_path = datadir["strings.prop"]

                # ...

    When the ``test_func()`` function asks for the ``data.txt`` resource, the
    following directories are searched for a file or directory named ``data.txt``,
    in this order:

    - ``tests/test_one/test_func/``
    - ``tests/test_one/``
    - ``tests/data/``

    The path to the first existing file (or directory) is returned as a
    :class:`py.path.local` object. In this case, the returned path would be
    ``tests/test_one/test_func/data.txt``.

    When the ``test_method()`` method asks for the ``strings.prop`` resource,
    the following directories are searched for a file or directory with the name
    ``strings.prop``, in this order:

    - ``tests/test_two/TestClass/test_method/``
    - ``tests/test_two/TestClass/``
    - ``tests/test_two/``
    - ``tests/data/``

    Here, this would return the path
    ``tests/test_two/TestClass/test_method/strings.prop``.

    As you can see, the searched directory hierarchy is slighly different if a
    *method* instead of a *function* asks for a resource. This allows you to
    load different resources based on the name of the test class, if you wish.

    Finally, if a test function or test method would ask for a resource named
    ``global.dat``, then the resulting path would be ``tests/data/global.dat``
    since no other directory in the searched directory hierarchy contains
    a file named ``global.dat``. In other words, the ``tests/data/`` directory
    is the place for global (or fallback) resources.

    If a resource cannot be found in *any* of the searched directories, a
    :class:`KeyError` is raised.
    """
    return _Datadir(request)
