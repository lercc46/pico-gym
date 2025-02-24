#!/bin/bash
exiftool -alldates='1970:01:01 00:00:00.001+00:00' \
	-subsectime=001 \
	-subsectimeoriginal=001 \
	-subsectimedigitized=001 \
	-filemodifydate='1970:01:01 00:00:00.001+00:00' original_modified.jpg
