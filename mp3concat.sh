#!/bin/bash

# Create a new file list for ffmpeg
rm -f filelist.txt
for f in *.mp3; do
    echo "file '$PWD/$f'" >> filelist.txt
done

# Concatenate the files using ffmpeg
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp3

# Clean up
rm filelist.txt
