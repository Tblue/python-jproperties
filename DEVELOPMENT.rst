Development Environment
=======================

Supported Python versions
-------------------------

See `tox.ini <./tox.ini>`_.

Running tests
-------------

Suggestion 1
~~~~~~~~~~~~

We have a GitHub Actions Workflow that runs the tests against all supported Python versions, so just
push your changes to your own branch, and let the CI system run the tests.

Suggestion 2
~~~~~~~~~~~~

With a bit of manual work, you can also run the tests locally:

Use `pyenv <https://github.com/pyenv/pyenv>`_, and install all the versions supported by the plugin.
Double-check on `tox.ini <./tox.ini>`_.

.. code-block:: shell
    pyenv install 2.7.18

    pyenv install 3.5.9

    pyenv install 3.6.10

    pyenv install 3.7.7

    pyenv install 3.8.3

Set the installed versions as global, that will allow tox to find all of them.

.. code-block:: shell

    pyenv global 2.7.18 3.5.9 3.6.10 3.7.7 3.8.3

Create virtualenv, install dependencies, run tests, and tox:

.. code-block:: shell

    python3.8 -m venv .python_jproperties

    source .python_jproperties/bin/activate

    pip install --upgrade setuptools pip tox

    python setup.py install

    python setup.py test

    tox

The development environment is complete.
