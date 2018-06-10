.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. spelling::

  cmake
  app

.. _project layout:

Project layout
--------------

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/fruits>`__
  * `Latest ZIP <https://github.com/cgold-examples/fruits/archive/master.zip>`__

+----------+--------------+---------------------------------------------------------------------+
| lib/     | *<project>/* | **<project>.hpp**                                                   |
+----------+--------------+-------------+-------------------------------------------------------+
|                         | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
|                         |             +-------------------------------------------------------+
|                         |             | **<target>.hpp**                                      |
+----------+--------------+-------------+-------------------------------------------------------+
| app/     | *<project>/* | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
+----------+--------------+-------------+-------------------------------------------------------+
| test/    | *<project>/* | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
+----------+--------------+-------------+-------------------------------------------------------+
| example/ | *<project>/* | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
+----------+--------------+-------------+-------------------------------------------------------+
| cmake/   | module/      | **<project>_<module>.cmake**                                        |
|          +--------------+---------------------------------------------------------------------+
|          | template/    | **\*.cmake.in**                                                     |
|          +--------------+---------------------------------------------------------------------+
|          | script/      | **\*.cmake**                                                        |
|          +--------------+---------------------------------------------------------------------+
|          | include/     | **\*.cmake**                                                        |
+----------+--------------+---------------------------------------------------------------------+

.. seealso::

  * :ref:`Install layout <install layout>`

.. code-block:: none

  ├── CMakeLists.txt
  ├── lib/
  │   ├── CMakeLists.txt
  │   └── fruits/
  │       ├── CMakeLists.txt
  │       ├── fruits.hpp
  │       ├── rosaceae/
  │       │   ├── CMakeLists.txt
  │       │   ├── rosaceae.hpp
  │       │   ├── Pear.cpp
  │       │   ├── Pear.hpp
  │       │   ├── Plum.cpp
  │       │   ├── Plum.hpp
  │       │   └── unittest/
  │       │       └── Pear.cpp
  │       └── tropical/
  │           ├── CMakeLists.txt
  │           ├── tropical.hpp
  │           ├── Avocado.cpp
  │           ├── Avocado.hpp
  │           ├── Pineapple.cpp
  │           ├── Pineapple.hpp
  │           └── unittest/
  │               ├── Avocado.cpp
  │               └── Pineapple.cpp
  ├── app/
  │   ├── CMakeLists.txt
  │   └── fruits/
  │       ├── CMakeLists.txt
  │       ├── breakfast/
  │       │   ├── CMakeLists.txt
  │       │   ├── flatware/
  │       │   │   ├── Teaspoon.cpp
  │       │   │   └── Teaspoon.hpp
  │       │   └── main.cpp
  │       └── dinner/
  │           ├── CMakeLists.txt
  │           └── main.cpp
  ├── example/
  │   ├── CMakeLists.txt
  │   └── fruits/
  │       ├── CMakeLists.txt
  │       ├── quick_meal/
  │       │   ├── CMakeLists.txt
  │       │   └── main.cpp
  │       └── vegan_party/
  │           ├── CMakeLists.txt
  │           └── main.cpp
  └── test/
      ├── CMakeLists.txt
      └── fruits/
          ├── CMakeLists.txt
          ├── check_tropical/
          │   ├── CMakeLists.txt
          │   └── data/
          │       └── avocado.ini
          └── skin_off/
              └── CMakeLists.txt
