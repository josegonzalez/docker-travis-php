=================
docker-travis-php
=================

Shits out a simple dockerfile for php projects based upon a .travis.yml

Literally don't use this and assume it'll work. It probably won't. Hence the description.

Literally the worst. I can't even.

Installation
============

Using PIP via PyPI::

    pip install docker-travis-php

Using PIP via Github::

    pip install git+git://github.com/josegonzalez/docker-travis-php.git#egg=docker-travis-php

Usage
=====

In a directory with a ``.travis.yml``, run the following:

.. code:: bash

    docker-travis-php

You will now have a ``Dockerfile`` in that directory that can be run via the following command:

.. code:: bash

    # builds the ``before_script`` and ``script`` sections
    # useful for "local" travis runs
    docker build .

The default debian packages that are installed (before php extensions) are as follows:

- ``git-core``
- ``libcurl4-openssl-dev``
- ``libicu-dev``
- ``php-pear``
- ``php5-cli``

You can add more by using the following environment variable:

.. code:: bash

    export PACKAGES=wget
    docker-travis-php

By default, the following extensions are built:

- ``curl``
- ``intl``
- ``mbstring``
- ``mysql``
- ``redis``
- ``xdebug``

You can configure this using the following environment variable:

.. code:: bash

    export EXTENSIONS=curl,intl,mbstring
    docker-travis-php
