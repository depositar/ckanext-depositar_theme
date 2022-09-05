=======================
ckanext-depositar_theme
=======================

This extension includes some visual customizations for depositar.

------------
Requirements
------------

This extension is only tested in CKAN 2.9 and later.

------------
Installation
------------

To install ckanext-depositar_theme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-depositar_theme Python package into your virtual environment::

     pip install -e 'git+https://github.com/depositar/ckanext-depositar_theme.git#egg=ckanext-depositar_theme'

3. Add ``depositar_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/ckan.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload
