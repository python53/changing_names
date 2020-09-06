#!/usr/bin/env python3

import sys
import subprocess

y=open(sys.argv[1], "r")

for line in y.readlines():
  old_name = line.strip()
  new_name = old_name.replace("name_old", "name_new")
  subprocess.run(["mv", old_name, new_name])
y.close





