#! /bin/bash

mode=$2
filename=./$1
#echo $filename
if [ ! -f $filename ]
then
    echo "File Not Found\n"
    exit 0
fi
echo $mode
if [ -z "$mode" ]
then
    index=1
    start=1
    echo "Fetching video formats...\n\n"
    for video in `cat $filename`
    do
        if [ $index -eq $start ]
        then
            pytube $video -l
            echo "\n-------------------------------------------------------\n\nPlease select an itag to select the desired format for downloading...\n\n"
            read format
        fi
        echo "\n[$index] Downloding $video with format $format"
        pytube $video --itag=$format
        index=$((index+1))
    done
else if [ $mode = playlist ]
then
    echo "Playlist not supported yet"
else
    echo "Invalid Mode"
fi
fi
exit 0
