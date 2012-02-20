#!/bin/bash

dir=cleaneddata
if [ ! -d $dir ]; then
	mkdir $dir
	echo "mkdir $dir"
	sleep 1
fi	

n=$( ls $dir | wc -w )
((n++))

for i in $( find $1 -type f )
do
	if [ ! ${i: -5} = "NOTES" ]; then
		cp $i $dir/data$n.txt
		((n++))
	fi
done
