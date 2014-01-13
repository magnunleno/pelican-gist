===================
Pelican Gist Plugin
===================

Pelican Gist is a plugin to enabled you to embed gists videos in your pages
and articles.

Usage
=====

In your article or page, you simply need to add a line to embed your gist.

.. code-block:: rst

    .. gist:: gist_id

Which will result in adding all files from this gist. If you whish to insert a single file from this gist, use the following attribute:

.. code-block:: rst

    .. gist:: gist_id
        :file: my_awsome_file.py

License
=======

`GPLv3`_ license.

.. GPLv3: http://gplv3.fsf.org/
