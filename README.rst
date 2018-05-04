Pygments C++ with User Defined Types
====================================

This is an extension of C++ lexer that just permits to add some user defined
types (classes, structs, etc.) to be displayed in the same manner as built-in
(plain) types.



Install
+++++++

Manual
------

::

    $ git clone git://github.com/vivenzio/pygments-udt.git
    $ cd pygments-udt
    $ (sudo) python setup.py install


Using
+++++

Just use the configuration file to add user defined types to be displayed in the
same way as "ordinary" types.


Using in LaTeX documents
++++++++++++++++++++++++

See the minted package at http://minted.googlecode.com.


Extra information
+++++++++++++++++

Pygments supported languages
----------------------------

Pygments at the moment supports over 150 different programming languages,
template languages and other markup languages. To see an exhaustive list of the
currently supported languages, use the command::

    $ pygmentize -L lexers

Pygments styles avaible
-----------------------

To get a list of all available stylesheets, execute the following command on the
command line::

    $ pygmentize -L styles

Please read the `official documentation`_ for further information on the usage
of pygment styles.

.. _official documentation: http://pygments.org/docs/
