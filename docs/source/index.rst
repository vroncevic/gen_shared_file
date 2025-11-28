Generate shared file modules
==============================

**gen_shared_file** is toolset for generation of shared file skeleton for
development embedded applications.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_shared_file python checker| |gen_shared_file python package| |github issues| |documentation status| |github contributors|

.. |gen_shared_file python checker| image:: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_python_checker.yml

.. |gen_shared_file python package| image:: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_shared_file.svg
   :target: https://github.com/vroncevic/gen_shared_file/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_shared_file.svg
   :target: https://github.com/vroncevic/gen_shared_file/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-shared-file/badge/?version=latest
   :target: https://gen-shared-file.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|gen_shared_file python3 build|

.. |gen_shared_file python3 build| image:: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_shared_file/releases

To install **gen_shared_file** type the following

.. code-block:: bash

    tar xvzf gen_shared_file-x.y.z.tar.gz
    cd gen_shared_file-x.y.z/
    #python3
    python3 setup.py install_lib
    python3 setup.py install_data
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen-shared-file

Dependencies
-------------

**gen_shared_file** tool-module requires other modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_shared_file** is based on Template mechanism

Generator structure

.. code-block:: bash

    gen_shared_file/
          ├── conf/
          │   ├── gen_shared_file.logo
          │   ├── gen_shared_file.cfg
          │   ├── gen_shared_file_util.cfg
          │   ├── project.yaml
          │   └── template/
          │       ├── shared_file.template
          │       ├── shared_file_lock.template
          │       ├── shared_file_unlock.template
          │       ├── write_shared_file.template
          │       └── read_shared_file.template
          ├── __init__.py
          ├── log/
          │   └── gen_shared_file.log
          ├── pro/
          │   ├── __init__.py
          │   ├── read_template.py
          │   └── write_template.py
          └── run/
              └── gen_shared_file_run.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2019 - 2026 by `vroncevic.github.io/gen_shared_file <https://vroncevic.github.io/gen_shared_file>`_

**gen_shared_file** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_shared_file/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`