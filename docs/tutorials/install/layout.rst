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
