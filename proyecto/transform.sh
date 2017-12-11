#!/bin/bash

path="audio/"
wavpath="audio/rock/"

for file in audio/*.mp3;
do
	filename=$(basename "$file")
	#echo $filename
	name="${filename%.*}"
	echo $file
	echo "$wavpath$name.mp3"
	sox "$file"  "$wavpath$name.mp3" trim 60 30
    #if [[ -f $file ]]; then

        #copy stuff ....
    #fi
done


