.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. spelling::

  cmake

.. _install layout:

Layout
------

+----------+--------------+------------------------------------------+
| include/ | *<project>/* | **<project>.hpp**                        |
+----------+--------------+------------------------------------------+
| lib*/    | **<project>_<target>**                                  |
|          +--------------+--------------+---------------------------+
|          | cmake/       | *<project>/* | **<project>Config.cmake** |
+----------+--------------+--------------+---------------------------+
| bin/     | **<project>_<target>**                                  |
+----------+--------------+------------------------------------------+
| cmake/   | module/      | **<project>_<module>.cmake**             |
|          +--------------+--------------+---------------------------+
|          | template/    | *<project>/* | **\*.cmake.in**           |
|          +--------------+--------------+---------------------------+
|          | script/      | *<project>/* | **\*.cmake**              |
+----------+--------------+--------------+---------------------------+

.. code-block:: cmake


  include(GNUInstallDirs)

  install(
      TARGETS <project>_<target>_1 <project>_<target>_2
      EXPORT <project>Targets
      LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
      ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
      RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
      INCLUDES DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
  )

.. seealso::

  * :ref:`Project layout <project layout>`

.. admonition:: CMake documentation

  * `GNUInstallDirs <https://cmake.org/cmake/help/latest/module/GNUInstallDirs.html>`__

Linux layout after installation of
`example project <https://github.com/cgold-examples/fruits>`__:

.. code-block:: none

  ├── bin/
  │   ├── fruits_breakfast*
  │   └── fruits_dinner*
  ├── include/
  │   └── fruits/
  │       ├── fruits.hpp
  │       ├── rosaceae/
  │       │   ├── Pear.hpp
  │       │   ├── Plum.hpp
  │       │   └── rosaceae.hpp
  │       └── tropical/
  │           ├── Avocado.hpp
  │           ├── Pineapple.hpp
  │           └── tropical.hpp
  └── lib/
      ├── cmake/
      │   └── fruits/
      │       ├── fruitsConfig.cmake
      │       ├── fruitsConfigVersion.cmake
      │       ├── fruitsTargets.cmake
      │       └── fruitsTargets-release.cmake
      ├── libfruits_rosaceae.a
      └── libfruits_tropical.a

Windows layout after installation of
`example project <https://github.com/cgold-examples/fruits>`__:

.. code-block:: none

  ├── bin/
  │   ├── fruits_breakfast.exe
  │   └── fruits_dinner.exe
  ├── include/
  │   └── fruits/
  │       ├── fruits.hpp
  │       ├── rosaceae/
  │       │   ├── Pear.hpp
  │       │   ├── Plum.hpp
  │       │   └── rosaceae.hpp
  │       └── tropical/
  │           ├── Avocado.hpp
  │           ├── Pineapple.hpp
  │           └── tropical.hpp
  └── lib/
      ├── cmake/
      │   └── fruits/
      │       ├── fruitsConfig.cmake
      │       ├── fruitsConfigVersion.cmake
      │       ├── fruitsTargets.cmake
      │       └── fruitsTargets-release.cmake
      ├── fruits_rosaceae.lib
      └── fruits_tropical.lib
