.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _include modules:

Include modules
===============

CMake modules is a common way to reuse code.

Include standard
~~~~~~~~~~~~~~~~

CMake comes with set of
`standard modules <https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html>`__:

.. literalinclude:: /examples/cmake-sources/include-processor-count/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 6

.. code-block:: shell
  :emphasize-lines: 2, 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hinclude-processor-count -B_builds
  Number of processors: 4
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

.. admonition:: CMake documentation

  * `ProcessorCount <https://cmake.org/cmake/help/latest/module/ProcessorCount.html>`__

.. warning::

  Do not include ``Find*.cmake`` modules such way. ``Find*.cmake`` modules
  designed to be used via
  `find_package <https://cmake.org/cmake/help/latest/command/find_package.html>`__.

Include custom
~~~~~~~~~~~~~~

You can modify ``CMAKE_MODULE_PATH`` variable to add the path with your
custom CMake modules:

.. literalinclude:: /examples/cmake-sources/include-users/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 8

.. literalinclude:: /examples/cmake-sources/include-users/modules/MyModule.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: shell
  :emphasize-lines: 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hinclude-users -B_builds
  Hello from MyModule!
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

.. admonition:: CMake documentation

  * `CMAKE_MODULE_PATH <https://cmake.org/cmake/help/latest/variable/CMAKE_MODULE_PATH.html>`__

.. _module name recommendation:

Recommendation
++++++++++++++

To avoid conflicts of your modules with modules from other projects (if they
are mixed together by ``add_subdirectory``) do "namespace" their names with the
project name:

.. code-block:: cmake
  :emphasize-lines: 6, 8

  cmake_minimum_required(VERSION 2.8)
  project(foo)

  list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules")

  include(tool_verifier) # BAD! What if parent project already has 'tool_verifier'?

  include(foo_tool_verifier) # Good, includes "./cmake/Modules/foo_tool_verifier.cmake"

.. seealso::

  * `OpenCV modules <https://github.com/opencv/opencv/tree/5f30a0a076e57c412509becd1fb618170cbfa179/cmake>`__

.. seealso::

  * :ref:`Function names <function name recommendation>`
  * :ref:`Cache names <cache name recommendation>`

Modify correct
~~~~~~~~~~~~~~

Note that the correct way to set this path is to **append** it to existing
value:

.. literalinclude:: /examples/cmake-sources/modify-path/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 8, 10

For example when user want to use his own modules instead of standard for
any reason:

.. literalinclude:: /examples/cmake-sources/modify-path/standard/ProcessorCount.cmake
  :language: cmake
  :emphasize-lines: 4-5

Works fine:

.. code-block:: shell
  :emphasize-lines: 3-4

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hmodify-path -B_builds "-DCMAKE_MODULE_PATH=`pwd`/modify-path/standard"
  Force processor count
  Number of processors: 16
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

Modify incorrect
~~~~~~~~~~~~~~~~

It's not correct to set them ignoring current state:

.. literalinclude:: /examples/cmake-sources/modify-incorrect/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

In this case if user want to use custom modules:

.. literalinclude:: /examples/cmake-sources/modify-incorrect/standard/ProcessorCount.cmake
  :language: cmake
  :emphasize-lines: 4-5

They will **not** be loaded:

.. code-block:: shell
  :emphasize-lines: 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hmodify-incorrect -B_builds "-DCMAKE_MODULE_PATH=`pwd`/modify-incorrect/standard"
  Number of processors: 4
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

Variables
~~~~~~~~~

Information about any kind of listfile can be taken from
``CMAKE_CURRENT_LIST_FILE`` and ``CMAKE_CURRENT_LIST_DIR`` variables:

.. literalinclude:: /examples/cmake-sources/path-to-module/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 8

.. literalinclude:: /examples/cmake-sources/path-to-module/cmake/mymodule.cmake
  :language: cmake
  :emphasize-lines: 3-4

.. code-block:: shell
  :emphasize-lines: 3-4

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hpath-to-module -B_builds
  Full path to module: /.../cmake-sources/path-to-module/cmake/mymodule.cmake
  Module located in directory: /.../cmake-sources/path-to-module/cmake
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

CMAKE_CURRENT_LIST_DIR vs CMAKE_CURRENT_SOURCE_DIR
++++++++++++++++++++++++++++++++++++++++++++++++++

The difference between those two variables is about type of information they
provide. ``CMAKE_CURRENT_SOURCE_DIR`` variable describe **source tree** and
should be read as *current source tree directory*.
Here is a list of sibling variables describing source/binary trees:

* CMAKE_SOURCE_DIR
* CMAKE_BINARY_DIR
* PROJECT_SOURCE_DIR
* PROJECT_BINARY_DIR
* **CMAKE_CURRENT_SOURCE_DIR**
* CMAKE_CURRENT_BINARY_DIR

The next files **always** exist:

* ``${CMAKE_SOURCE_DIR}/CMakeLists.txt``
* ``${CMAKE_BINARY_DIR}/CMakeCache.txt``
* ``${PROJECT_SOURCE_DIR}/CMakeLists.txt``
* ``${CMAKE_CURRENT_SOURCE_DIR}/CMakeLists.txt``

``CMAKE_CURRENT_LIST_DIR`` variable describe **current listfile** (it is not
necessary ``CMakeLists.txt``, it can be ``somemodule.cmake``), should
be read as *directory of currently processed listfile*, i.e.
directory of ``CMAKE_CURRENT_LIST_FILE``. Here is another list of sibling
variables:

* CMAKE_CURRENT_LIST_FILE
* CMAKE_CURRENT_LIST_LINE
* **CMAKE_CURRENT_LIST_DIR**
* CMAKE_PARENT_LIST_FILE

.. admonition:: Stackoverflow

  * `What is the difference between CMAKE_CURRENT_SOURCE_DIR and CMAKE_CURRENT_LIST_DIR? <http://stackoverflow.com/q/15662497/2288008>`__

Example
+++++++

Assume we have external CMake module that calculates SHA1 of CMakeLists.txt
and save it with some custom info to ``sha1`` file in current binary directory:

.. literalinclude:: /examples/cmake-sources/with-external-module/external/mymodule.cmake
  :language: cmake

``mymodule.cmake`` use some resource. Resource ``info/message.txt``
is a file with content:

.. literalinclude:: /examples/cmake-sources/with-external-module/external/info/message.txt
  :language: none

To read this resource we must use ``CMAKE_CURRENT_LIST_DIR`` because file
located **in same external directory** as module:

.. literalinclude:: /examples/cmake-sources/with-external-module/external/mymodule.cmake
  :language: cmake
  :emphasize-lines: 3

To read CMakeLists.txt we must use ``CMAKE_CURRENT_SOURCE_DIR`` because
CMakeLists.txt located **in source directory**:

.. literalinclude:: /examples/cmake-sources/with-external-module/external/mymodule.cmake
  :language: cmake
  :emphasize-lines: 4

Subdirectory ``boo`` use those module:

.. literalinclude:: /examples/cmake-sources/with-external-module/example/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8

.. code-block:: shell

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hwith-external-module/example -B_builds -DCMAKE_MODULE_PATH=`pwd`/with-external-module/external
  Top level CMakeLists.txt
  Processing foo/CMakeList.txt
  Processing boo/CMakeList.txt
  Processing boo/baz/CMakeLists.txt
  Processing boo/bar/CMakeLists.txt
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

Check ``sha1`` file created by module:

.. code-block:: shell
  :emphasize-lines: 4

  [cmake-sources]> cat _builds/boo/sha1
  Message from external module

  sha1(CMakeLists.txt) = 9f0ceda4ca514a074589fc7591aad0635b6565eb

Verify value manually:

.. code-block:: shell
  :emphasize-lines: 2

  [cmake-sources]> openssl sha1 with-external-module/example/boo/CMakeLists.txt
  SHA1(with-external-module/example/boo/CMakeLists.txt)= 9f0ceda4ca514a074589fc7591aad0635b6565eb

Here is diagram that will make everything clear:

.. image:: images/with-external-module.png
  :align: center

Recommendation
++++++++++++++

Use ``CMAKE_CURRENT_LIST_DIR`` variable for navigation. Note that in function
this variable is set to the directory where function **used**, not where
function **defined** (see :ref:`function <function list dir>` for details).
Use ``CMAKE_CURRENT_BINARY_DIR`` for storing manually generated files.

.. warning::

  Do not use ``CMAKE_CURRENT_BINARY_DIR`` for figuring out the full path
  to objects that was build by native tool, e.g. using
  ``${CMAKE_CURRENT_BINARY_DIR}/foo.exe`` is a bad idea since for Linux
  executable will be named ``${CMAKE_CURRENT_BINARY_DIR}/foo`` and for multi
  configuration generators it will be like
  ``${CMAKE_CURRENT_BINARY_DIR}/Debug/foo.exe`` and really should be determined
  on a build step instead of generate step. In such cases
  :doc:`generator expressions </tutorials/generator-expressions>` is helpful.
  For example
  `$<TARGET_FILE:tgt> <https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html#informational-expressions>`__.

Make sure you **totally** understand what each variable mean in other scenarios:

* ``CMAKE_SOURCE_DIR``/``CMAKE_BINARY_DIR`` these variables point to the root
  of the source/binary trees. Paths that use such variables will change their
  location if your project will be used as a subproject. They will point to the
  **parent** project, not yours.

* ``PROJECT_SOURCE_DIR``/``PROJECT_BINARY_DIR`` these variables are better
  then previous but still kind of a global nature. You should change all paths
  related to ``PROJECT_SOURCE_DIR`` if you decide to move declaration of
  your project or decide to detach some part of the code and add new ``project``
  command in the middle of the source tree. Consider using extra variable
  with clean separate purpose for such job
  ``set(FOO_MY_RESOURCES "${CMAKE_CURRENT_LIST_DIR}/resources")``
  instead of referring to ``${PROJECT_SOURCE_DIR}/resources``.

* ``CMAKE_CURRENT_SOURCE_DIR`` this is a directory with ``CMakeLists.txt``.
  If you're using this variable internally you can substitute is with
  ``CMAKE_CURRENT_LIST_DIR``. In case you're creating module for external usage
  consider moving all functionality to ``function``.

With this recommendation previous example can be rewritten in next way:

.. literalinclude:: /examples/cmake-sources/with-external-module-good/external/mymodule.cmake
  :language: cmake
  :emphasize-lines: 3-5, 8-10

.. note::

  As you may notice we don't have to use ``_long_variable`` names since function
  has it's own scope.

And call ``mymodule`` function instead of including module:

.. literalinclude:: /examples/cmake-sources/with-external-module-good/example/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8

Effect is the same:

.. code-block:: shell

  [cmake-sources]> cat _builds/boo/sha1
  Message from external module

  sha1(CMakeLists.txt) = 36bcbf5f2f23995661ca4e6349e781160910b71f
  [cmake-sources]> openssl sha1 with-external-module-good/example/boo/CMakeLists.txt
  SHA1(with-external-module-good/example/boo/CMakeLists.txt)= 36bcbf5f2f23995661ca4e6349e781160910b71f
