#!/bin/bash
python3 main.py $1 > out
gedit out &
if [ $# > 1 ]
then 
xdg-open $1
fi