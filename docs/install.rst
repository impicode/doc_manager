############
Installation
############

===============
Package install
===============

Assuming you have django installed, the first step is to install module with pip::

    pip install git+ssh://git@bitbucket.org/impicode/doc-manager.git

for a specific branch::

    pip install git+ssh://git@bitbucket.org/impicode/doc-manager.git@branchname


==============
Basic settings
==============

in settings.py add doc_manager to INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'doc_manager',
    ]

=================
Optional settings
=================

``MAX_FILE_UPLOAD_SIZE`` setting::

    MAX_FILE_UPLOAD_SIZE = 1234

A number indicating the maximum file size allowed for upload.
    | 2.5MB - 2621440
    | 5MB - 5242880
    | 10MB - 10485760
    | 20MB - 20971520
    | 50MB - 52428800
    | 100MB - 104857600
    | 250MB - 214958080
    | 500MB - 429916160

``FILE_UPLOAD_TO`` setting::

    FILE_UPLOAD_TO = 'documents/%Y/%m/%d/'

A string indicating path for uploaded files.
