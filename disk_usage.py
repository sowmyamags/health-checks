#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
   """Rerturns True if there is enough free disk space, false otherwise"""
   du = shutil.disk_usage(disk)
   #Calculate the percentage of freespace
   percent_free = 100 * du.free / du.total
   # Calculate how many gigabytes
   gigabytes_free = du.free / 2**30
   if percent_free < min_percent or gigabytes_free < min_absolute:
      return False
   return True

#check for a least 2 GB and 10% free
if not check_disk_usage("/", 1, 10):
   print("ERROR: N0t enough disk usage")
   sys.exit(1)

print("Everything Ok")
sys.exit(0)
