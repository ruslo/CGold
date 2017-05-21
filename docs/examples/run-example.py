#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(
    description='Script for generating documentation from example'
)

parser.add_argument(
    '--example', help='Name of the directory with example', required=True
)

cmd_args = parser.parse_args()

example_dir = cmd_args.example
current_dir = os.getcwd()

if not os.path.isabs(example_dir):
  example_dir = os.path.join(current_dir, example_dir)

if not os.path.exists(example_dir):
  sys.exit('Directory not found: {}'.format(example_dir))

relative_example_dir = os.path.relpath(example_dir, current_dir)
top_dir, last_dir = os.path.split(current_dir)

print('Example full path: {}'.format(example_dir))
print('Example relative path: {}'.format(relative_example_dir))

sources_list = []

for top, dirs, files in os.walk(example_dir):
  for x in files:
    if x == 'commands.txt':
      continue
    to_add = os.path.join(top, x)
    print('Add to sources: {}'.format(to_add))
    sources_list.append(to_add)

doc_rst = os.path.join(top_dir, 'docs.rst')
doc_file = open(doc_rst, 'w')

for x in sources_list:
  doc_file.write(
      '.. literalinclude:: /examples/{}/{}\n'.format(
          last_dir, os.path.relpath(x, current_dir)
      )
  )
  doc_file.write('  :language: cmake\n')
  doc_file.write('  :emphasize-lines: 1-2, 3\n')
  doc_file.write('  :linenos:\n\n')

commands_file = os.path.join(example_dir, 'commands.txt')
if os.path.exists(commands_file):
  print('Using commands from file: {}'.format(commands_file))
  commands = open(commands_file, 'r').read().split('\n')
  commands.remove('')
else:
  commands = [
    'rm -rf _builds',
    'cmake -H{} -B_builds'.format(relative_example_dir)
  ]

doc_file.write('.. code-block:: none\n')
doc_file.write('  :emphasize-lines: 2, 4-5\n')
doc_file.write('  :linenos:\n\n')

for x in commands:
  print('Executing command: {}'.format(x))
  doc_file.write('  [{}]> {}\n'.format(last_dir, x))
  to_log = subprocess.check_output(
      x,
      shell=True,
      universal_newlines=True,
      stderr=subprocess.STDOUT
  )
  print('== OUTPUT BEGIN ==\n"{}"\n== OUTPUT END =='.format(to_log))
  to_log.rstrip('\n')
  log_lines = to_log.split('\n')
  if log_lines[-1] == '':
    log_lines = log_lines[:-1]
  for line in log_lines:
    line = line.replace(top_dir, '/...')
    doc_file.write('  ')
    doc_file.write(line)
    doc_file.write('\n')

doc_file.close()
doc_file = open(doc_rst, 'r')
print('=== DOCUMENTATION ===\n\n{}'.format(doc_file.read()))
