dblp-python
===========

A simple Python wrapper around the DBLP API, currently supporting author search and author and publication lookup.

Example
=======

Let's search for `Michael Ley`_, DBLP maintainer. Try ::

    >>> import dblp
    >>> #do a simple author search for michael ley
    >>> authors = dblp.search('michael ley')
    >>> michael = authors[0]
    >>> print michael.name
    Michael Ley
    >>> print len(michael.publications)
    31

If you'd like to learn more about Michael's work, you can explore his publications. All publication results are lazy-loaded, so have at it ::

   >>> print michael.publications[0].title
   DBLP - Some Lessons Learned.
   >>> print michael.publications[0].journal
   PVLDB
   >>> print michael.publications[0].year
   2009

More information about a publication can often be found at its `ee` URL - in this case, a link to the PDF ::

   >>> print michael.publications[0].ee
   http://www.vldb.org/pvldb/2/vldb09-98.pdf

Other publication and author attributes are documented with their respective classes- just use `help()`. Enjoy!

.. _Michael Ley: http://www.informatik.uni-trier.de/~ley/

Contributing
============

Contributions are very welcome! Feel free to fork the repo and request a pull, or open an issue if you find a bug or would like to request a feature.
