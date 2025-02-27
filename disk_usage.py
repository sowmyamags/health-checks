#!/usr/bin/env python3

import shutil
import sys
import os 

def check_reboot():
   """Returns True id the computer has a pending reboot."""
   return os.path.exists("/run/reboot.required")

def check_disk_full(disk, min_gb, min_percent):
   """Rerturns True if there is enough free disk space, false otherwise"""
   du = shutil.disk_usage(disk)
   #Calculate the percentage of free space
   percent_free = 100 * du.free / du.total
   # Calculate how many gigabytes
   gigabytes_free = du.free / 2**30
   if percent_free < min_percent or gigabytes_free < min_gb:
      return False
   return True

def check_root_full():
   """Returns True is the root partition is full, false otherwise."""
   return check_disk_full(disk ="/", min_gb=2, min_percent=10)

def main():
   checks = [(check_reboot, "Pending Reboot"), (check_root_full, "Root partition full")]
   
   everything_ok = True
   for check, msg in checks:
      if check():
         print(msg)
         everything_ok = False
   
   if not everything_ok:
      sys.exit(1)

   print("Everything ok.")
   sys.exit(0)


main()
