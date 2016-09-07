.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _project layout:

Project layout
--------------

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/fruits>`__
  * `Latest ZIP <https://github.com/cgold-examples/fruits/archive/master.zip>`__

+------------+------------------------------------------------------------------------------------+
| *cmake/*   | **<project>_<module>.cmake**                                                       |
+------------+--------------+-------------+-------------------------------------------------------+
| *lib/*     | *<project>/* | **<project>.hpp**                                                   |
+------------+--------------+-------------+-------------------------------------------------------+
|                           | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
|                           |             +-------------------------------------------------------+
|                           |             | **<target>.hpp**                                      |
+------------+--------------+-------------+-------------------------------------------------------+
| *app/*     | *<project>/* | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
+------------+--------------+-------------+-------------------------------------------------------+
| *test/*    | *<project>/* | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
+------------+--------------+-------------+-------------------------------------------------------+
| *example/* | *<project>/* | *<target>/* | **CMakeLists.txt** with target ``<project>_<target>`` |
+------------+--------------+-------------+-------------------------------------------------------+

.. seealso::

  * :ref:`Install layout <install layout>`
