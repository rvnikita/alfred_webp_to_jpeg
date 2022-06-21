#!/usr/bin/env python3

import os
import sys

old_fullfilename = sys.argv[1]
old_path = os.path.dirname(old_fullfilename) 
old_filename = os.path.basename(old_fullfilename)
old_filename_without_ext = os.path.splitext(old_filename)[0]


#check if new name is already exists
if os.path.exists(f"{old_path}/{old_filename_without_ext}.mp3"):
    number_counter = 1
    
    #iterate through name until fine the one that does not exist
    while os.path.exists(f"{old_path}/{old_filename_without_ext}({number_counter}).mp3"):
        number_counter = number_counter + 1
    new_filename = f"{old_filename_without_ext}({number_counter}).mp3"
else:
    new_filename = old_filename + ".mp3"
    
new_fullfilename = f"{old_path}/{new_filename}"
ffmpeg_command = f'/opt/homebrew/bin/ffmpeg -i "{old_fullfilename}" "{new_fullfilename}"'

os.system(ffmpeg_command)