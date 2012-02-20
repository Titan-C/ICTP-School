#!/bin/bash
dir=cleandat
mkdir $dir
find $1 -type f -exec cp -v {} $dir \;
rm $dir/NOTES

n=0
for i in $dir/*
do
   	mv -v $i $dir/sample$n.txt
       	((n++))
done
