# jProperties for Python 2

jProperties is a Java Property file parser and writer for Python 2. It aims to provide the same functionality
as Java's [Properties](http://docs.oracle.com/javase/7/docs/api/java/util/Properties.html) class, although currently the
XML property format is not supported.

## Overview

Objects of the type `Properties` can be used like a Python dictionary (but see [Caveats](#caveats) below).
The `load()` method populates the object by parsing a Java Property file; the `store()` method
writes the key-value pairs stored in the object to a file in the Java Property format.

The `load()` and `store()` methods both take an `encoding` parameter. By default this is set to `iso-8859-1`, but it
can be set to any encoding supported by Python, including e. g. the widely used `utf-8`.

## Special features

### Metadata

The property file parser supports including metadata in property files which can be read and set programmatically.
Metadata for a key is represented as a Python dictionary. This dictionary should only contains strings for the keys and
values, although when the property file is written, all non-string objects will be converted to strings. **This is a
one-way conversion**; when the metadata is read back again during a `load()`, all keys and values will be strings.

By default, the `store()` method does not write out metadata. To enable that feature, set the keyword argument
`strip_meta=False`.

#### Caveats

Metadata support influences how `Properties` objects can be used as dictionary objects:
- To set a value for a key, do `prop_object[key] = value` or `prop_object[key] = value, metadata`. The first form
  will leave the key's metadata unchanged. You can also use the `setmeta()` method to set a key's metadata.
- To get the value of a key, do `value, metadata = prop_object[key]`. If there is no metadata for a key,
  `metadata` will be an empty dictionary. To retrieve only the metadata for a key, the `getmeta()` method can be used.
- When used as an iterator, `Properties` objects will only return keys without metadata, as usual.

### Setting defaults

The internal dictionary holding the key-value pairs can be accessed using the `properties` property. Deleting that
property deletes all key-value pairs from the object.

However, modifying properties using this special property will **not** modify metadata in any way. That means that
deleting properties by doing `del prop_obj.properties[key]` will not remove the associated metadata from the object.
Instead, do `del prop_obj[key]`.

The `properties` property is still useful to set many default values before parsing a property file:
```python
prop_obj.properties = a_big_dictionary_with_defaults
prop_obj.load(file_object)
```