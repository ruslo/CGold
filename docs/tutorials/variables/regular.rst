.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Regular variables
-----------------

Regular vs cache
================

Unlike :ref:`cache variables <cache variables>` regular (normal) CMake variables
have scope and don't outlive CMake runs.

If in the next example you run the CMake configure step twice, without removing
the cache:

.. literalinclude:: /examples/usage-of-variables/cache-vs-regular/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7-8

.. literalinclude:: /examples/usage-of-variables/cache-vs-regular/configure.log
  :language: none
  :emphasize-lines: 3,12

You can see that the regular CMake variable ``abc`` is created from scratch
each time

.. literalinclude:: /examples/usage-of-variables/cache-vs-regular/configure.log
  :language: none
  :emphasize-lines: 4,6,13,15

And the cache variable ``xyz`` is created only once and reused on second run

.. literalinclude:: /examples/usage-of-variables/cache-vs-regular/configure.log
  :language: none
  :emphasize-lines: 5,7,14,16

You can find cache variable ``xyz`` in :ref:`CMakeCache.txt <cmakecache.txt>`:

.. code-block:: none

  [usage-of-variables]> grep xyz _builds/CMakeCache.txt
  xyz:STRING=321

Unlike regular ``abc``:

.. code-block:: none

  [usage-of-variables]> grep abc _builds/CMakeCache.txt
  [usage-of-variables]> echo $?
  1

Scope of variable
=================

Each variable is linked to the scope where it was defined. Commands
`add_subdirectory <https://cmake.org/cmake/help/latest/command/add_subdirectory.html>`__
and
`function <https://cmake.org/cmake/help/latest/command/function.html>`__
introduce their own scopes:

.. literalinclude:: /examples/usage-of-variables/directory-scope/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 10

.. literalinclude:: /examples/usage-of-variables/directory-scope/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

There are two variables ``abc`` defined. One in top level scope and another
in scope of ``boo`` directory:

.. code-block:: none
  :emphasize-lines: 2-5

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hdirectory-scope -B_builds
  Top level scope (before): 123
  Directory 'boo' scope: 456
  Top level scope (after): 123
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

New scope
=========

When a new scope is created it will be initialized with the variables of the parent
scope. Command `unset <https://cmake.org/cmake/help/latest/command/unset.html>`__
can remove a variable from the current scope. If a variable is not found in
the current scope it will be dereferenced to an empty string:

.. literalinclude:: /examples/usage-of-variables/take-from-parent-scope/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6,12,17,18

.. code-block:: none
  :emphasize-lines: 2-7

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Htake-from-parent-scope -B_builds
  Top level scope state: { abc = '123', xyz = '456' }
  [boo]: Scope for function 'boo' copied from parent: { abc = '123', xyz = '456' }
  [boo]: Command 'set(abc ...)' modify current scope, state: { abc = '789', xyz = '456' }
  [foo]: Scope for function 'foo' copied from parent 'boo': { abc = '789', xyz = '456' }
  [foo]: Command 'unset(abc)' will remove variable from current scope: { abc = '', xyz = '456' }
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

.. _same scope:

Same scope
==========

``include`` and ``macro`` don't introduce a new scope, so commands
like ``set`` and ``unset`` will affect the current scope:

.. literalinclude:: /examples/usage-of-variables/same-scope/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6,9,13,16,19

.. literalinclude:: /examples/usage-of-variables/same-scope/modify-abc.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: none
  :emphasize-lines: 2-6

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hsame-scope -B_builds
  abc (before): 123
  abc (after): 456
  xyz (before): 336
  xyz (after): 789
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

.. _parent scope:

Parent scope
============

A variable can be set to the parent scope by specifying ``PARENT_SCOPE``:

.. literalinclude:: /examples/usage-of-variables/parent-scope/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8

Variable **will only be set to parent** scope:

.. literalinclude:: /examples/usage-of-variables/parent-scope/configure.log
  :emphasize-lines: 4,7

Current scope will not be affected:

.. literalinclude:: /examples/usage-of-variables/parent-scope/configure.log
  :emphasize-lines: 5,6

As well as parent of the parent:

.. literalinclude:: /examples/usage-of-variables/parent-scope/configure.log
  :emphasize-lines: 3,8

From cache
==========

If variable is not found in the current scope, it will be taken from
the cache:

.. literalinclude:: /examples/usage-of-variables/from-cache/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4,5,9

.. code-block:: none
  :emphasize-lines: 2-4

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hfrom-cache -B_builds
  Regular variable from current scope: 123
  Cache variable if regular not found: 789
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Cache unset regular
===================

Note that the order of commands is important because ``set(... CACHE ...)``
will remove the regular variable with the same name from current scope:

.. literalinclude:: /examples/usage-of-variables/cache-remove-regular/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4,5,9

.. code-block:: none
  :emphasize-lines: 2,3

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hcache-remove-regular -B_builds
  Regular variable unset, take from cache: 789
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

.. _cache confusing:

Confusing
=========

This may lead to a quite confusing behavior:

.. literalinclude:: /examples/usage-of-variables/cache-confuse/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6,10

In this example ``set(... CACHE ...)`` will remove ``abc`` only from scope of
function and not from top level scope:

.. code-block:: none
  :emphasize-lines: 2-5

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hcache-confuse -B_builds
  Function scope before cache modify = 123
  Function scope after cache modify = 789
  Parent scope is not affected, take variable from current scope, not cache = 123
  -- Configuring done
  -- Generating done
  -- build files have been written to: /.../usage-of-variables/_builds

This will be even more confusing if you run this example one more time without
removing cache:

.. code-block:: none
  :emphasize-lines: 1-4

  [usage-of-variables]> cmake -Hcache-confuse -B_builds
  Function scope before cache modify = 123
  Function scope after cache modify = 123
  Parent scope is not affected, take variable from current scope, not cache = 123
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Since variable ``abc`` already stored in cache command ``set(... CACHE ...)``
has no effect and **will not remove** regular ``abc`` from scope of function.

Names
=====

Variable names are case-sensitive:

.. literalinclude:: /examples/usage-of-variables/case-sensitive/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-6, 8-10

.. code-block:: none
  :emphasize-lines: 2-8

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hcase-sensitive -B_builds
  a: 123
  b: 567
  aBc: 333
  A: 321
  B: 765
  ABc: 777
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Name of variable may consist of **any** characters:

.. literalinclude:: /examples/usage-of-variables/any-names/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-9

.. code-block:: none
  :emphasize-lines: 2-8

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hany-names -B_builds
  Variable name: 'abc', value: '123'
  Variable name: 'ab c', value: '456'
  Variable name: 'ab?c', value: '789'
  Variable name: '/usr/bin/bash', value: '987'
  Variable name: 'C:\Program Files\', value: '654'
  Variable name: ' ', value: '321'
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Quotes
======

In the previous example, the quote character ``"`` was used to create a name containing
a space - this is called *quoted argument*. Note that the argument must start and end
with a quote character, otherwise it becomes an *unquoted argument*. In this case, the
quote character will be treated as part of the string:

.. literalinclude:: /examples/usage-of-variables/quotes/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-6

.. code-block:: none
  :emphasize-lines: 3-8

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hquotes -B_builds
  a = 'Quoted argument'
  b = 'x-"Unquoted argument"'
  c =
    'x"a'
    'b'
    'c"'
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

As you can see the variable ``b`` contains quotes now and for list ``c`` quotes
are part of the elements: ``x"a``, ``c"``.

.. admonition:: CMake documentation

 * `Quoted argument <https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument>`__
 * `Unquoted argument <https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument>`__

Dereferencing
=============

Dereferenced variable can be used in creation of new variable:

.. literalinclude:: /examples/usage-of-variables/dereference/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

.. literalinclude:: /examples/usage-of-variables/dereference/configure.log
  :emphasize-lines: 3

Or new variable name:

.. literalinclude:: /examples/usage-of-variables/dereference/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7

.. literalinclude:: /examples/usage-of-variables/dereference/configure.log
  :emphasize-lines: 4

Or even both:

.. literalinclude:: /examples/usage-of-variables/dereference/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8

.. literalinclude:: /examples/usage-of-variables/dereference/configure.log
  :emphasize-lines: 5

Nested dereferencing
====================

Dereferencing of variable by ``${...}`` will happen as many times as needed:

.. literalinclude:: /examples/usage-of-variables/nested-dereference/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5,7

.. code-block:: none
  :emphasize-lines: 2,17-26

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hnested-dereference -B_builds
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
  -- Check for working C compiler: /usr/bin/cc
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Check for working CXX compiler: /usr/bin/c++
  -- Check for working CXX compiler: /usr/bin/c++ -- works
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  Compiler for language C: /usr/bin/cc
  Flags for language C + build type DEBUG: -g
  Flags for language C + build type RELEASE: -O3 -DNDEBUG
  Flags for language C + build type RELWITHDEBINFO: -O2 -g -DNDEBUG
  Flags for language C + build type MINSIZEREL: -Os -DNDEBUG
  Compiler for language CXX: /usr/bin/c++
  Flags for language CXX + build type DEBUG: -g
  Flags for language CXX + build type RELEASE: -O3 -DNDEBUG
  Flags for language CXX + build type RELWITHDEBINFO: -O2 -g -DNDEBUG
  Flags for language CXX + build type MINSIZEREL: -Os -DNDEBUG
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Types of variable
=================

Variables always have type string but some commands can interpret them
differently.  For example the command ``if`` can treat strings as boolean, path, target
name, etc.:

.. literalinclude:: /examples/usage-of-variables/types-of-variable/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4,5,7,9

.. code-block:: none
  :emphasize-lines: 2,17-20

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Htypes-of-variable -B_builds
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
  -- Check for working C compiler: /usr/bin/cc
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Check for working CXX compiler: /usr/bin/c++
  -- Check for working CXX compiler: /usr/bin/c++ -- works
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  condition_a
  NOT condition_b
  File exists: /.../usage-of-variables/types-of-variable/CMakeLists.txt
  Target exists: foo
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

.. admonition:: CMake documentation

  * `if <https://cmake.org/cmake/help/latest/command/if.html>`__

Create list
===========

Some commands can treat a variable as list. In this case the string
value is split into elements separated by ``;``.
The command ``set`` can create such lists:

.. literalinclude:: /examples/usage-of-variables/list/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-8

``set`` creates **string** from elements and puts the ``;`` between them:

.. literalinclude:: /examples/usage-of-variables/list/configure.log
  :emphasize-lines: 3

In case you want to add an element with space you can protect the element
with ``"``:

.. literalinclude:: /examples/usage-of-variables/list/configure.log
  :emphasize-lines: 5

As seen with ``l4`` variable protecting ``;`` with ``"`` doesn't have any
effect:

.. literalinclude:: /examples/usage-of-variables/list/configure.log
  :emphasize-lines: 7

We are concatenating **string** ``a`` with **string** ``b;c`` and putting
``;`` between them. Final result is the **string** ``a;b;c``.  When
a command interprets this string as list, such list has 3 elements.
Hence **it's not a list** with two elements ``a`` and ``b;c``.

The command ``message`` interprets ``l3`` as list with 3 elements, so in the end
4 arguments (value of type string) passed as input:
``print by message:_``, ``a``, ``b``, ``c``. Command ``message`` will concatenate
them without any separator, hence string ``print by message: abc`` will be
printed:

.. literalinclude:: /examples/usage-of-variables/list/configure.log
  :emphasize-lines: 8-9

.. admonition:: CMake documentation

  * `set <https://cmake.org/cmake/help/latest/command/set.html>`__

Operations with list
====================

The ``list`` command can be used to calculate length of list, get element by index,
remove elements by index, etc.:

.. literalinclude:: /examples/usage-of-variables/list-operations/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-6, 8-10, 16, 20

.. code-block:: none
  :emphasize-lines: 2-8

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hlist-operations -B_builds
  length of 'a;b;c' (l0) = 3
  length of 'a;b;c' (l1) = 3
  length of 'a;b c' (l2) = 2
  l1[2] = c
  Removing first item from l1 list: 'a;b;c'
  l1 = 'b;c'
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

.. admonition:: CMake documentation

  * `list <https://cmake.org/cmake/help/latest/command/list.html>`__

Empty list
==========

Since list is really just a string there is no such object as
"list with one empty element". Empty string is a list with no elements -
length is 0. String ``;`` is a list with two empty elements - length is 2.

Historically result of appending empty element to an empty list is an empty
list:

.. literalinclude:: /examples/usage-of-variables/empty-list/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13-14, 20-21, 27-28

.. code-block:: none
  :emphasize-lines: 4-16, 19-31, 34-46

  [examples]> rm -rf _builds
  [examples]> cmake -Husage-of-variables/empty-list -B_builds

  Adding non-empty element to non-empty list.

  Add 'c' to list 'a;b'
  Result: 'a;b;c' (length = 3)

  Add 'c' to list 'a;b;c'
  Result: 'a;b;c;c' (length = 4)

  Add 'c' to list 'a;b;c;c'
  Result: 'a;b;c;c;c' (length = 5)

  Add 'c' to list 'a;b;c;c;c'
  Result: 'a;b;c;c;c;c' (length = 6)


  Adding empty element to non-empty list.

  Add '' to list 'a;b'
  Result: 'a;b;' (length = 3)

  Add '' to list 'a;b;'
  Result: 'a;b;;' (length = 4)

  Add '' to list 'a;b;;'
  Result: 'a;b;;;' (length = 5)

  Add '' to list 'a;b;;;'
  Result: 'a;b;;;;' (length = 6)


  Adding empty element to empty list.

  Add '' to list ''
  Result: '' (length = 0)

  Add '' to list ''
  Result: '' (length = 0)

  Add '' to list ''
  Result: '' (length = 0)

  Add '' to list ''
  Result: '' (length = 0)

  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../examples/_builds

Recommendation
==============

Use **short laconic lower-case** names (``a``, ``i``, ``mylist``, ``objects``,
etc.) for local variables that used **only by the current scope**. Use **long
detailed upper-case** names (``FOO_FEATURE``, ``BOO_ENABLE_SOMETHING``, etc.)
for variables that used by **several scopes**.

For example it make no sense to use long names in function since function
has it's own scope:

.. code-block:: cmake

  function(foo_something)
    set(FOO_SOMETHING_A 1)
    # ...
  endfunction()

Using just ``a`` will be fine:

.. code-block:: cmake

  function(foo_something)
    set(a 1)
    # ...
  endfunction()

Same with scope of :ref:`CMakeLists.txt <cmakelists.txt>`:

.. code-block:: cmake

  # Foo/CMakeLists.txt

  message("Files:")
  foreach(FOO_FILES_ITERATOR ${files})
    message("  ${FOO_FILES_ITERATOR}")
  endforeach()

Prefer instead:

.. code-block:: cmake

  # Foo/CMakeLists.txt

  message("Files:")
  foreach(x ${files})
    message("  ${x}")
  endforeach()

.. seealso::

  * :ref:`Cache names <cache name recommendation>`

Compare it with C++ code:

.. code-block:: cpp

  // pretty bad idea
  #define a

  // good one
  #define MYPROJECT_ENABLE_A

.. code-block:: cpp

  // does it make sense?
  for (int array_iterator = 0; array_iterator < array.size(); ++array_iterator) {
    // use 'array_iterator'
  }

  // good one
  for (int i = 0; i < array.size(); ++i) {
    // use 'i'
  }

Summary
=======

* All variables have a **string** type
* List is nothing but **string**, elements of list separated by ``;``
* The way how variables are interpreted **depends on the command**
* Do not give same names for **cache** and **regular** variables
* ``add_subdirectory`` and ``function`` create **new scope**
* ``include`` and ``macro`` work in the **current scope**
