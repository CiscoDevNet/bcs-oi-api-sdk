=============================
BCS Operational Insights APIs
=============================

*Example consumer script of the Business Critical Services APIs*

.. image:: https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg
    :target: https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/bcs-apis
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/CiscoDevNet/bcs-apis/blob/master/LICENSE
.. image:: https://img.shields.io/pypi/v/bcs-apis.svg
    :target: https://pypi.python.org/pypi/bcs-apis

-------------------------------------------------------------------------------

Business Critical Services Operational Insights APIs

Example
-------

.. code-block:: python

    from bcsapis import BCSApis

    bcs_api = BCSApis(
        client_id='client id',
        client_secret='client secret',
        server='api-cx.cisco.com')
    )

    psirt_details = bcs_api.get_product_alerts_psirt()
    psirt_bulletins = bcs_api.get_product_alerts_psirt_bulletins()


Installation
------------

Installing and upgrading is easy:

**Install via PIP**

.. code-block:: bash

    $ pip install bcsapis

**Upgrading to the latest Version**

.. code-block:: bash

    $ pip install bcsapis --upgrade


Questions, Support & Discussion
-------------------------------

bcsapis_ is a *community developed* and *community supported* project. Feedback, thoughts, questions, issues can be submitted using the issues_ page.

Contribution
------------

bcsapis_ is a *community developed* project. Code contributions are welcome via PRs!

*Copyright (c) 2018-2021 Cisco and/or its affiliates.*


.. _bcsapis: https://github.com/CiscoDevNet/bcs-apis
.. _issues: https://github.com/CiscoDevNet/bcs-apis/issues
.. _format: https://docs.python.org/3/library/shutil.html#shutil.make_archive
