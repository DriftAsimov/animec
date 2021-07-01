Animec | Documentation
==================================

Description
-----------

``animec`` is an open source python module to scrape information about anime characters, info, news, lyrics and more. It scrapes results from `MyAnimeList <https://myanimelist.net/>`__. The anilyrics class uses `animesonglyrics <https://www.animesonglyrics.com/>`__ to return the lyrics.

.. warning::

   This module requires Python 3.6 or above to work properly.

Highlights
----------

- Easily get anime characters's info
- Retrieve anime info
- Get suitable recommendations based on votes
- Get anime lyrics in Kanji, Romaji and English

More features are being worked on!

Installation
------------

Using pip
~~~~~~~~~
.. code-block::
   
   # Linux/macOS
   python3 -m pip install -U animec

   # Windows
   py -3 -m pip install -U animec

Manually
~~~~~~~~
.. code-block::

   $ git clone https://github.com/DriftAsimov/animec
   $ cd animec
   $ python3 setup.py install

.. note::

   A ratelimit has been added to avoid stressing the module. If that ratelimit is bypassed, then you risk getting your IP banned temporarily from making requests. So it's recommended not to try any such practice.

.. toctree::
   :maxdepth: 1
   :caption: Classes and methods

   ./anime
   ./anilyrics
   ./aninews
   ./charsearch
   ./kao
   ./exceptions


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
