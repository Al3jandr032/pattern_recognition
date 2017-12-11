#!/bin/bash

path="audio/"
rockpath="audio/rock/"
metalpath="audio/metal/"
poppath="audio/pop/"
electropath="audio/electro/"

for file in $electropath*.mp3;
do
	
	filename=$(basename "$file")
	fname="${filename%.*}"
	echo $fname
	#echo $file
		
	mpg123 -w "$electropath/wav/$fname.wav" "$file"

done
