Changelog
=========

Version 3.0.0 (UNRELEASED)
++++++++++++++++++++++++++

Breaking changes
****************

- Drop support for Python versions older than 3.8. Most notably, this means
  that Python 2.7 is not supported anymore either.

Improvements
************

- Build process modernization:

  - Use ``pyproject.toml`` instead of ``setup.py``.
  - Use modern ``setuptools_scm`` version (fixes `#15`_).
- Sign GPG release tags (see README for details).

Version 2.1.2
+++++++++++++

- Set minium required Python version in package metadata.

This is the last version supporting Python 2.7.

**Note:** Code for this release can be found on branch ``python2-legacy``,
although the only thing that changed in this release is the package metadata.

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

- This is the first "proper" PyPI release, with proper PyPI metadata and proper
  PyPI distributions.  Nothing else has changed.

Version 1.0
+++++++++++

- Initial release


.. _Documenting Properties: ./README.rst#documenting-properties
.. _#5: https://github.com/Tblue/python-jproperties/pull/5
.. _#1: https://github.com/Tblue/python-jproperties/pull/1
.. _#10: https://github.com/Tblue/python-jproperties/pull/10
.. _#13: https://github.com/Tblue/python-jproperties/pull/13
.. _#14: https://github.com/Tblue/python-jproperties/pull/14
.. _#15: https://github.com/Tblue/python-jproperties/issues/15


.. vim: tw=79
