Create SharedFile project skeleton
------------------------------------

**gen_shared_file** is tool for creating SharedFile project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

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

   self
   modules

🚀 Installation
------------------

|gen_shared_file python3 build| |gen_shared_file interface checker| |gen_shared_file isp checker| |gen_shared_file srp checker|

.. |gen_shared_file python3 build| image:: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_python3_build.yml

.. |gen_shared_file interface checker| image:: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_interface_checker.yml

.. |gen_shared_file isp checker| image:: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_isp_checker.yml

.. |gen_shared_file srp checker| image:: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_file/actions/workflows/gen_shared_file_srp_checker.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_shared_file/releases

To install **gen_shared_file** type the following

.. code-block:: bash

    tar xvzf gen_shared_file-x.y.z.tar.gz
    cd gen_shared_file-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_shared_file-*-py3-none-any.whl
    rm -f get-pip.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install gen_shared_file

📦 Dependencies
-----------------

**gen_shared_file** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-------------------

**gen_shared_file** is based on OOP.

Tool structure

.. code-block:: bash

    gen_shared_file/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_shared_file_command_definition.py
         │   │   ├── gen_shared_file_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_shared_file.cfg
         │   │   ├── gen_shared_file.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 44 files

✨ Features
-------------

* Automatically scaffolds C/C++ shared file project files.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

📊 Code coverage
------------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
----------

Install package

.. code-block:: bash

    pip3 install gen_shared_file

Prepare main entry point by downloading `main.py` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_shared_file/main/main.py

Running tool for creating new SharedFile project skeleton

.. code-block:: bash

    python3 main.py create --name mytool --type base --output ./demo/

📚 Docs
----------

More documentation and info at

* `gen_shared_file.readthedocs.io <https://gen-shared-file.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
-----------------

`Contributing to gen_shared_file <https://github.com/vroncevic/gen_shared_file/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
--------------------------

|gpl v3 license| |apache 2.0 license|

Copyright (C) 2025 - 2026 by `vroncevic.github.io/gen_shared_file <https://vroncevic.github.io/gen_shared_file>`_

**gen_shared_file** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

|donate|

.. |gpl v3 license| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |apache 2.0 license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_shared_file/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://www.python.org/psf/donations/
