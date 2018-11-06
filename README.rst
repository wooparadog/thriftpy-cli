Thriftpy-Cli
=============

Install
========

.. code:: bash

    pip install thriftpy-cli

If you are using Python2, ipython 7 and above has dropped python2 support, so you'll need:

.. code:: bash

   pip install thriftpy-cli ipython==6.5.0

Usage
=====

.. code:: bash

    $ thriftpy-cli -t thrift_file.thrift -h localhost -p 8010 -s ServiceName
    $ # Launching into ipython
    >>> client.api(*args)
