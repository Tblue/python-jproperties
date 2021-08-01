jProperties for Python |pypi-badge|
===================================

jProperties is a Java Property file parser and writer for Python. It aims to provide the same functionality
as `Java's Properties class <http://docs.oracle.com/javase/7/docs/api/java/util/Properties.html>`_, although
currently the XML property format is not supported.

.. sectnum::
.. contents:: **Table of Contents**

Installation
------------

You can install jProperties using `pip <https://pip.pypa.io/>`_::

    pip install jproperties

Overview
--------

Objects of the type ``Properties`` can be used like a Python dictionary (but see Caveats_ below).
The ``load()`` method populates the object by parsing input in the Java Property file format; the ``store()``
method writes the key-value pairs stored in the object to a stream in the same format.

The ``load()`` and ``store()`` methods both take an ``encoding`` parameter. By default this is set to
``iso-8859-1``, but it can be set to any encoding supported by Python, including e. g. the widely used
``utf-8``.

Parsing a property file
+++++++++++++++++++++++

.. code:: python

    from jproperties import Properties

    p = Properties()
    with open("foobar.properties", "rb") as f:
        p.load(f, "utf-8")

That's it, ``p`` now can be used like a dictionary containing properties from ``foobar.properties``.

Writing a property file
+++++++++++++++++++++++

.. code:: python

    from jproperties import Properties

    p = Properties()
    p["foobar"] = "A very important message from our sponsors: Python is great!"

    with open("foobar.properties", "wb") as f:
        p.store(f, encoding="utf-8")

Reading from and writing to the same file-like object
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: python

    from jproperties import Properties

    with open("foobar.properties", "r+b") as f:
        p = Properties()
        p.load(f, "utf-8")

        # Do stuff with the p object...

        f.seek(0)
        f.truncate(0)
        p.store(f, encoding="utf-8")

Special features
----------------

Metadata
++++++++

The property file parser supports including programmatically readable and settable metadata in property files.
Metadata for a key is represented as a Python dictionary; the keys and values of this dictionary should be strings,
although when the property file is written, all non-string objects will be converted to strings. **This is a
one-way conversion**; when the metadata is read back again during a ``load()``, all keys and values will be treated
as simple strings.

By default, the ``store()`` method does not write out the metadata. To enable that feature, set the keyword argument
``strip_meta=False`` when calling the method.

Note that metadata support is always enabled. The only thing that is optional is actually writing out the metadata.

Metadata keys beginning with two underscores (``__``) are not written to the output stream by the ``store()`` method.
Thus, they can be used to attach "runtime-only" metadata to properties. Currently, however, metadata with such keys is
still read from the input stream by ``load()``; this should probably be considered erroneous behaviour.

Documenting Properties
^^^^^^^^^^^^^^^^^^^^^^

The comments after a property definition can be added to the metadata
with the key ``_doc`` if the ``metadoc=True`` optional argument is given
to the ``load`` method.  This allows properties to be documented in the
properties file.  For example, the properties file::

    #: _severity=fatal
    10001=Fatal internal error: %s
    # A fatal internal error occurred.  Please re-run the command
    # with the -D option to generate additional debug information.

The following example code shows how this documentation can be accessed.

.. code:: python

    from jproperties import Properties

    p = Properties()
    with open("foobar.properties", "rb") as f:
        p.load(f, "utf-8", metadoc=True)
    # Print the explicitly defined '_severity' metadata
    print("Severity: ", p.getmeta("10001")['_severity'])
    # Print the implicitly defined '_doc' metadata
    print("Explanation: ", p.getmeta("10001")['_doc'])

The documentation can be extracted from properties files and used to generate
pages in the overall system documentation or can be accessed via options
for command line utilities.

Caveats
^^^^^^^

Metadata support influences how ``Properties`` objects are used as dictionary objects:

- To set a value for a key, do ``prop_object[key] = value`` or ``prop_object[key] = value, metadata``. The first form
  will leave the key's metadata unchanged. You can also use the ``setmeta()`` method to set a key's metadata.
- To get the value of a key, do ``value, metadata = prop_object[key]``. If there is no metadata for a key,
  ``metadata`` will be an empty dictionary. To retrieve only the metadata for a key, the ``getmeta()`` method can
  be used.
- When used as an iterator, ``Properties`` objects will simply return all keys in an unspecified order. No metadata is
  returned (but can be retrieved using  ``getmeta()``).

Setting defaults
++++++++++++++++

The internal dictionary holding the key-value pairs can be accessed using the ``properties`` property. Deleting that
property deletes all key-value pairs from the object.

However, modifying properties using this special property will **not** modify metadata in any way. That means that
deleting properties by doing ``del prop_obj.properties[key]`` will not remove the associated metadata from the object.
Instead, do ``del prop_obj[key]``.

The ``properties`` property is nevertheless useful to set many default values before parsing a property file:

.. code:: python

    from jproperties import Properties

    prop_obj = Properties()
    prop_obj.properties = a_big_dictionary_with_defaults
    file_obj = codecs.open("foobar.properties", "rb", "iso-8859-1")
    prop_obj.load(file_obj, encoding=None)


Development
++++++++++++++++

If you want to help development, there is
`overview documentation <./DEVELOPMENT.rst>`_

Version history
---------------

Version 2.1.1
+++++++++++++

- Compatibility with Python 3.10. (`#10`_)
- Documentation improvements. (`#13`_)
- Support decoding surrogate pairs on narrow Python builds (such as
  Python 2.7 on Mac OS X). (`#14`_)

Version 2.1.0
+++++++++++++

- Add support for optional documentation comments (see `Documenting
  Properties`_). Thanks to @mkrohan! (`#5`_)

Version 2.0.0
+++++++++++++

- **Python 3 support!** Thanks to @tboz203, who did a lot of the work. (`#1`_)
- Drop support for Python 2.6.

Version 1.0.1
+++++++++++++

- This is the first "proper" PyPI release, with proper PyPI metadata and proper PyPI distributions.
  Nothing else has changed.

Version 1.0
+++++++++++

- Initial release


.. _#5: https://github.com/Tblue/python-jproperties/pull/5
.. _#1: https://github.com/Tblue/python-jproperties/pull/1
.. _#10: https://github.com/Tblue/python-jproperties/pull/10
.. _#13: https://github.com/Tblue/python-jproperties/pull/13
.. _#14: https://github.com/Tblue/python-jproperties/pull/14

..
    NB: Without a trailing question mark in the following image URL, the
        generated HTML will contain an <object> element instead of an <img>
        element, which apparently cannot be made into a link (i. e. a
        "clickable" image).
.. |pypi-badge| image:: https://img.shields.io/pypi/v/jproperties.svg?
    :align: middle
    :target: https://pypi.python.org/pypi/jproperties
