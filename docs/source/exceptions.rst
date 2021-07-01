Exceptions
==========

All of the exceptions raised by the module.

.. toctree::
   :maxdepth: 3
   :caption: Exceptions
 
.. automodule:: animec.errors
   :members:
   :show-inheritance:

They can be easily handled using try except blocks in this way:

Handling
--------

.. code-block::
   
   try:
      result = animec.Anime('foo')
   except animec.errors.NoResultFound:
      print("No such anime found in the search query.")
