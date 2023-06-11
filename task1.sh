#!/bin/bash
echo "LETS GO"
#to get the file name and location
read folder_permission
#locate the file / directory 
locate -b folder_permission
#changing permsions to read + write write and write could use 644
chmod rw-r--r-- folder_permission
echo " Task Complete"