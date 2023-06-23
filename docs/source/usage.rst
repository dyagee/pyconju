Using PyConju
=============

.. _using PyConju:

**PyConju** is a Python package that can effortlessly merge multiple file formats (XLSX, XLS, CSV) into a single file, saving you valuable time and effort. It's the go-to tool for data analysts, scientists, and anyone working with complex datasets.

.. _installation:

Installation
------------

To use PyConju, first install it using pip:

.. code-block:: console

   (.venv) $ pip install pyonju

.. _usage:

Basic Usage
----------------

Merging Excel .xlsx files
^^^^^^^^^^^^^^^^^^^^^^^^^^

Provide a list of the filenames and the directory path:

.. code-block:: python

  from pyconju.xlsx import Excelx

  # Initialize object; don't add closed brackets
  merger = Excelx
  path = "path/to/files/to/merge"
  fileList = ["file1.xlsx","file2.xlsx","file3.xlsx"]
  merger.merge_xlsx(fileList,path)

Merging Excel .xls files
^^^^^^^^^^^^^^^^^^^^^^^^

Provide a list of the filenames and the directory path:

.. code-block:: python

   from pyconju.xls import Excel

   # Initialize object
   merger = Excel
   path = "path/to/files/to/merge"
   fileList = ["file1.xls","file2.xls","file3.xls"]
   merger.merge_xls(fileList,path)

If there is an error such as:

.. code-block:: console

   ImportError: Pandas requires version '2.0.1' or newer of 'xlrd' (version '1.2.0' currently installed).

Uninstall the current version of ``xlrd``:

.. code-block:: console

   (.venv) $ pip uninstall xlrd

   Found existing installation: xlrd 1.2.0
   Uninstalling xlrd-1.2.0:


   Proceed (Y/n)? y
   Successfully uninstalled xlrd-1.2.0 


Install ``xlrd`` version ``2.0.1``:

.. code-block:: console

   (.venv) $ pip install xlrd==2.0.1

.. tip::
   Try the merging process again; it will work 🤩


.. note::
   The above error is taken care of, as from ``pyconju 0.1.2`` and latest releases.



Merging  CSV files
^^^^^^^^^^^^^^^^^^

Provide a list of the filenames and the directory path:

.. code-block:: python

   from pyconju.csv import Csv

   # Initialize object 
   merger = Csv
   path = "path/to/files/to/merge"
   fileList = ["file1.xlsx","file2.xlsx","file3.xlsx"]
   merger.merge_csv(fileList,path)

.. note::
   The ``invalid_files`` are  ``skipped``  and if only   ``file`` is passed in the fileList, the  ``output`` will be same.

.. _Supported File Types:

Supported File Types
---------------------

PyConju supports ``.xls``, ``.xlsx`` and ``.csv`` for now. Check for future releases...

.. _Dependency:

Dependency
----------------

PyConju depends heavily on ``pandas``, do well to check `pandas Documentation`_.

.. _pandas Documentation: https://pandasguide.readthedocs.io/en/latest/ 




Tracking Bugs
----------------

If you run into ``issues``, do well to visit the :ref:`contributing`  section for more details. 

If you have already read the guidlines, log the ``issue`` directly  on the  `github repo`_.

.. _github repo: https://github.com/dyagee/pyconju/issues



