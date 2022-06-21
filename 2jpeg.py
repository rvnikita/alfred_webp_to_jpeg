#!/usr/bin/env python3

import os
import sys

old_fullfilename = sys.argv[1]
old_path = os.path.dirname(old_fullfilename) 
old_filename = os.path.basename(old_fullfilename)
old_filename_without_ext = os.path.splitext(old_filename)[0]


#check if new name is already exists
if os.path.exists(f"{old_path}/{old_filename_without_ext}.jpeg"):
    number_counter = 1
    
    #iterate through name until fine the one that does not exist
    while os.path.exists(f"{old_path}/{old_filename_without_ext}({number_counter}).jpeg"):
        number_counter = number_counter + 1
    new_filename = f"{old_filename_without_ext}({number_counter}).jpeg"
else:
    new_filename = old_filename + ".jpeg"
    
new_fullfilename = f"{old_path}/{new_filename}"
magick_command = f'/opt/homebrew/bin/magick convert "{old_fullfilename}" "{new_fullfilename}"'

os.system(magick_command)