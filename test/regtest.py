#! /usr/bin/env python

import subprocess
import re

# list of regression tests with the expected outputs
tests = [
  ('simple', r'1 verified, 0 errors'),
  ('simple_fail', r'0 verified, 1 error')
]


for test in tests:

  # invoke SMACK
  p = subprocess.Popen(['smack.py', test[0], '-o', test[0] + '.bpl'], stdout=subprocess.PIPE)
  smackOutput = p.communicate()[0]

  # check SMACK output
  if re.search(test[1], smackOutput):
    print 'PASSED: ', test[0]
  else:
    print 'FAILED: ', test[0]

