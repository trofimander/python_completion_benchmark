# Given this `sys.path` root structure:
#
# syspath_root1/
#   nspkg1/
#     m1.py
# syspath_root2/
#   nspkg1/
#     m2.py

import nspkg1  # nspkg1
import nspkg1.m1  # m1
import nspkg1.m2  # m2