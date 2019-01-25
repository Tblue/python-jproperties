- Implement the dict method ``copy()``. Need to preserve key order, though,
  which leads to the following TODO item.
- Use ``OrderedDict`` for the internal properties dict, and drop the ``_key_order``
  attribute.
- ``__getitem__()`` and ``__setitem__()`` should not return metadata anymore.
  There's ``getmeta()`` and ``setmeta()`` for that, and it is confusing if you
  set a non-tuple value using ``__setitem__()``, but then get back a tuple
  when calling ``__getitem__()``.

- More tests for edge cases.
- Add tests to ensure that we provide necessary dict methods.

- Support line continuation in escape sequences. This means that e. g.
  ``\uXX<newline><whitespace>XX`` and ``\uXXXX<newline>\uXXXX`` are
  valid, the latter being a surrogate pair. The easiest solution would be
  to process line continuations on the (currently non-existing) lexer level.
