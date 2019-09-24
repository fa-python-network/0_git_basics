#!/bin/bash

TN=docs-monthly 
#TN=docs-weekly
#TN=docs-daily

OF=$TN.tar.gz

LOGFILE=/var/log/backup.log

echo  >>$LOGFILE
echo "====================================================="  >>$LOGFILE
echo "$(date +'%d-%b-%Y %R')" >>$LOGFILE
echo "Задание \"$TN\" запущено..." >>$LOGFILE

OLD_IFS=$IFS

IFS=$'\n'

SRCD="/mnt/source/folder_1
/mnt/source/folder_2
/mnt/source/folder_N"

TGTD="/var/backups/"
TGTD2="/mnt/archive/"

tar -czf $TGTD$OF $SRCD &>>$LOGFILE
#tar -u -f $TGTD$OF $SRCD &>>$LOGFILE

STATUS=$?

IFS=$OLD_IFS

if [[ $STATUS != 0 ]]; then
    rm $TGTD$OF &>>$LOGFILE
    echo "###########################################" >>$LOGFILE
    echo "###  Произошла ошибка! Бэкап не удался. ###" >>$LOGFILE
    echo "###########################################" >>$LOGFILE
    echo "$(date +'%d-%b-%Y %R%nФайл') бекапа $OF не создан" | sendxmpp -t -f /usr/local/etc/XMPP_settings логин_получателя@домен &>>$LOGFILE
else
    echo "Файл бэкапа сохранен как \"$TGTD$OF\"" >>$LOGFILE
    echo "Бэкап успешно завершен в $(date +'%R %d-%b-%Y')!" >>$LOGFILE
    echo "Монтирование файловой системы для резервного архива $TGTD_archive" >>$LOGFILE
    mount $TGTD2 &>>$LOGFILE
    if [[ $? != 0 ]]; then
        echo "#############################################################" >>$LOGFILE
        echo "###  Произошла ошибка при монтировании резервного ресурса ###" >>$LOGFILE
        echo "#############################################################" >>$LOGFILE
        echo "$(date +'%d-%b-%Y %R%nФайл') бекапа $OF не скопирован на резервный ресурс" | sendxmpp -t -f /usr/local/etc/XMPP_settings логин_получателя@домен &>>$LOGFILE
        exit
    fi
    echo "Начато копирование файла на резервный ресурс" >>$LOGFILE
    cp -f $TGTD$OF $TGTD_archive$OF &>>$LOGFILE
    if [[ $? != 0 ]]; then
        echo "#############################################################" >>$LOGFILE
        echo "###  Произошла ошибка при копировании на резервный ресурс ###" >>$LOGFILE
        echo "#############################################################" >>$LOGFILE
        echo "$(date +'%d-%b-%Y %R%nФайл') бекапа $OF не скопирован на резервный ресурс" | sendxmpp -t -f /usr/local/etc/XMPP_settings логин_получателя@домен &>>$LOGFILE
    else
        echo "Копирование файла успешно завершено  в $(date +'%R %d-%b-%Y')!" >>$LOGFILE
        echo "Файл скопирован как \"$TGTD_archive$OF\"" >>$LOGFILE
    fi
    echo "Размонтирование файловой системы для резервного архива $TGTD_archive" >>$LOGFILE
    umount $TGTD2 &>>$LOGFILE
    echo "Все операции завершены успешно!" >>$LOGFILE
fi
tail -n 300  $LOGFILE >/tmp/unique_fantastic_filename.tmp
mv -f /tmp/unique_fantastic_filename.tmp $LOGFILE
exit