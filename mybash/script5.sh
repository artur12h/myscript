#! /bin/bash

counter=0
while [ $counter -lt 10 ]; do
	echo "Current counter is $counter"
	counter=$(($counter+1))
done

for myfile in 'ls *.txt'; do
      cat $myfile
done

for x in { 1..10 }
	echo "X = $x "
done
