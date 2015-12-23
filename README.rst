jProperties for Python 2
========================

jProperties is a Java Property file parser and writer for Python 2. It aims to provide the same functionality
as `Java's Properties class <http://docs.oracle.com/javase/7/docs/api/java/util/Properties.html>`_, although
currently the XML property format is not supported.

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

    p = Properties()
    with open("foobar.properties", "rb") as f:
        p.load(f, "utf-8")

That's it, ``p`` now can be used like a dictionary containing properties from ``foobar.properties``.

Writing a property file
+++++++++++++++++++++++

.. code:: python

    p = Properties()
    p["foobar"] = "A very important message from our sponsors: Python is great!"

    with open("foobar.properties", "wb") as f:
        p.store(f, encoding="utf-8")

Reading from and writing to the same file-like object
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: python

    with open("foobar.properties", "r+b") as f:
        p = Properties()
        p.load(f, "utf-8")

        # Do stuff with the p object...

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

    prop_obj.properties = a_big_dictionary_with_defaults
    file_obj = codecs.open("foobar.properties", "rb", "iso-8859-1")
    prop_obj.load(file_obj)

Version history
---------------

Version 1.0.1
+++++++++++++

- This is the first "proper" PyPI release, with proper PyPI metadata and proper PyPI distributions.
  Nothing else has changed.

Version 1.0
+++++++++++

- Initial release