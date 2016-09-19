.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _install layout:

Layout
------

+------------+--------------+--------------------------------------+
| *cmake/*   | *<project>/* | **<project>_<module>.cmake**         |
+------------+--------------+--------------------------------------+
| *include/* | *<project>/* | **<project>.hpp**                    |
+------------+--------------+--------------------------------------+
| *lib/*     | **<project>_<target>**                              |
|            +----------+--------------+---------------------------+
|            | *cmake/* | *<project>/* | **<project>Config.cmake** |
+------------+----------+--------------+---------------------------+
| *bin/*     | **<project>_<target>**                              |
+------------+-----------------------------------------------------+

.. code-block:: cmake

  install(
      TARGETS <project>_<target>_1 <project>_<target>_2
      EXPORT <project>Targets
      LIBRARY DESTINATION "lib"
      ARCHIVE DESTINATION "lib"
      RUNTIME DESTINATION "bin"
      INCLUDES DESTINATION "include"
  )

.. seealso::

  * :ref:`Project layout <project layout>`

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
