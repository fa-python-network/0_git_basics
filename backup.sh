#!/bin/bash

#Напишите скрипт который и считает кол-во уникальных записей из какого-нибудь лога (access.log, auth.log) и выводит на экран.

yfile="/var/log/auth.log"
res=$(sort $yfile | uniq -u | wc -l)
echo "Количество уникальных строк в файле $yfile - $res"
