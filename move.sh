#!/bin/bash
cd ./data
while [ -n "$1" ] #проходим через все поданные скрипту аргументы
do
	mv *.$1 ../tabs
	shift
done
