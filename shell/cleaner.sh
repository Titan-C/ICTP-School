#!/bin/bash

#Create a new directory to store data in case it doesn't exist allready
dir=cleaneddata
if [ ! -d $dir ]; then
	mkdir $dir
	echo "mkdir $dir"
	sleep 1
fi	

#Count already existing files inside $dir 
n=$( ls $dir | wc -w )
((n++))

#loop trough data file for copying
for i in $( find $1 -type f )
do
	if [ ! ${i: -5} = "NOTES" ]; then
		cp $i $dir/data$n.txt
		((n++))
	fi
done
