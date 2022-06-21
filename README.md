# alfred_2jpeg
Python script for Alfred to convert webp, heic to jpeg

# Requirements
installed ffmpeg and located in /usr/local/bin/ffmpeg
intsalled python3
installed magick

# Setup
Run through /bin/bash and '/usr/bin/python3 /Users/rvnikita/dev/webp2jpeg/2jpeg.py $1' command where if the full path to 2jpeg.py script

# Alfred Structure
File Action → Run Script

Script to iterate through several files

```
for f in "$@"
do
	/usr/local/bin/python3 /Users/rvnikita/dev/webp2jpeg/2jpeg.py "$f"
	>&2 echo "$f"
done
```

# Alfred shortcut
In OSX finder press option + command + \
