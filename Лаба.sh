#!/bin/bash
START=$(date +%s)

function exit_program {
	END=$(date +%s)
	runtime=$(( $END - $START ))
	if [ "$time" = "1" ]; then
		printf "\e[1;32m-----------------------------------------------\e[0m\n"
		printf "\e[1;32m|    Время выполнения программы: %.0f cекунд     |\e[0m\n" $runtime
	fi
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	printf "\e[1;32m|             Выход из программы              |\e[0m\n"
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	exit
}

function help_console {
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	printf "\e[1;32m|             Парсинг Access Log              |\e[0m\n"
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	echo "Для работы программы необходимо указать название файла"
	echo "Пример: bash $0 access_log.txt"
	echo ""
	echo "Ключи"
	echo "  -count         Показывает сколько записей Access Log успешно обработала программа"
	echo "  -code code     Фильтрация по коду завершения операции"
	echo "  -url code      Фильтрация по URL адресу"
	echo "  -rsize         Подсчитать количество байт в выведенных строках"
	echo "  -ip address    Фильтрация по IP адресу с которого выполнялся запрос"
	echo "  -protocol name Фильтрация по HTTP протоколу"
	echo "  -reverse       Включить обратная сортировка строк"
	echo "  -time          Перед завершением программы показать время выполения работы"			
	echo "  -interactive   Запуск интерактивного режима"
	echo "  -help        	 Справка"
	echo "Пример: bash $0 -count -time -code 404 access_log.txt"
	echo ""
	echo "Так же можно указать необязательный параметр – код заверешения операции используемый для дальнейшей фильтрации"
	echo "Пример: bash $0 access_log.txt 404"
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
}

function help_interactive_console {
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	printf "\e[1;32m|       Команды интерактивного режима         |\e[0m\n"
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	if [ "$count" = "1" ]; then
		printf "(\e[1;32mВключено\e[0m) 1 – Показ колличества записей Access Log успешно отработанных программой\n"
	else
		printf "(\e[1;31mВыключено\e[0m) 1 – Показ колличества записей Access Log успешно отработанных программой\n"
	fi
	if [ "$code" = "0" ]; then
		printf "(\e[1;31mНет кода\e[0m) 2 - Фильтрация по коду завершения\n"
	else
		printf "(\e[1;32mКод: $code\e[0m) 2 - Фильтрация по коду завершения\n"
	fi
	if [ "$ip" = "0" ]; then
		printf "(\e[1;31mНет IP\e[0m) 3 - Фильтрация по IP адресу\n"
	else
		printf "(\e[1;32mIP: $ip\e[0m) 3 - Фильтрация по IP адресу\n"
	fi
	if [ "$url" = "0" ]; then
		printf "(\e[1;31mНет URL\e[0m) 4 - Фильтрация по URL адресу с которого выполнялся запрос\n"
	else
		printf "(\e[1;32mURL: $url\e[0m) 4 - Фильтрация по URL адресу с которого выполнялся запрос\n"
	fi
	if [ "$protocol" = "0" ]; then
		printf "(\e[1;31mНет HTTP протокола\e[0m) 5 - Фильтрация по имени HTTP протокола\n"
	else
		printf "(\e[1;32mHTTP: $protocol\e[0m) 5 - Фильтрация по имени HTTP протокола\n"
	fi
	if [ "$rsize" = "1" ]; then
		printf "(\e[1;32mВключено\e[0m) 6 – Подсчет переданных байт в выведенных строках\n"
	else
		printf "(\e[1;31mВыключено\e[0m) 6 – Подсчет переданных байт в выведенных строках\n"
	fi
	if [ "$reverse" = "1" ]; then
		printf "(\e[1;32mВключено\e[0m) 7 – Обратный вывод строк\n"
	else
		printf "(\e[1;31mВыключено\e[0m) 7 – Обратный вывод cтрок\n"
	fi
	printf "–– Напишите \e[1;32mY\e[0m или \e[1;32mSTART\e[0m для запуска парсинга ––\n"
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
}

function commandCheck {
	if [ "$arg" = "Y" -o "$arg" = "y" -o "$arg" = "0" -o "$arg" = "START"  -o "$arg" = "Start"  -o "$arg" = "start" ]; then
		MENU=0
	fi
	if [ "$arg" = "1" ]; then
		if [ "$count" = "1" ]; then
			count=0
		else
			count=1
		fi
	fi
	if [ "$arg" = "2" ]; then
		read -p "Укажите код для фильтрации(0 для отмены): " code
	fi
	if [ "$arg" = "3" ]; then
		read -p "Укажите IP для фильтрации(0 для отмены): " ip
	fi
	if [ "$arg" = "4" ]; then
		read -p "Укажите URL для фильтрации(0 для отмены): " url
	fi
	if [ "$arg" = "5" ]; then
		read -p "Укажите название HTTP протокола для фильтрации(0 для отмены): " protocol
	fi
	if [ "$arg" = "6" ]; then
		if [ "$rsize" = "1" ]; then
			rsize=0
		else
			rsize=1
		fi
	fi
	if [ "$arg" = "7" ]; then
		if [ "$reverse" = "1" ]; then
			reverse=0
		else
			reverse=1
		fi
	fi
}

function readFile {
	echo "-----------------------------------------------"
	read -p "Укажите действительный путь к файлу: " FILE
	checkFile
}

function checkFile {
	if [ -f "$FILE" ]; then
		printf "\e[1;32m-----------------------------------------------\e[0m\n"
		printf "\e[1;32m|                Файл найден!                 |\e[0m\n"
		printf "\e[1;32m-----------------------------------------------\e[0m\n"
	else
		readFile
	fi
}

function interactivMenuWhile {
	while [ "$MENU" != "0" ];
	do
		clear
		help_interactive_console
		read -p "Введите номер команды: " arg
		commandCheck
	done
}

function interactiveMode {
	clear
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	printf "\e[1;32m|  Программа запущена в интерактивном режиме  |\e[0m\n"
	printf "\e[1;32m-----------------------------------------------\e[0m\n"
	printf "Использовать файл log.txt? [\e[1;32mY\e[0m/(a)] "
	read answer
	if [ "$answer" = "Y" -o "$answer" = "y" -o "$answer" = "да" -o "$answer" = "Да" -o "$answer" = "Yes" -o "$answer" = "yes" ]; then
		FILE=log.txt
		checkFile
		interactivMenuWhile
	else
		echo "-----------------------------------------------"
		read -p "Укажите полный путь к файлу: " FILE
		checkFile
		interactivMenuWhile
	fi
}

reverse=0
count=0
code=0
url=0
rsize=0
protocol=0
ip=0
time=0
interactive=0
help=0
MENU=1

if [ $# -eq 0 ]
	then
		help_console
fi
while [ -n "$1" ]
	do
		case "$1" in
			-reverse)
				reverse=1;;
				
			-rsize)
				rsize=1;;
				
			-count)
				count=1;;
			
			-time)
				time=1;;

			-code)
				code="$2"
				shift;;
			
			-url)
				url="$2"
				shift;;
			
			-protocol)
				protocol="$2"
				shift;;
			
			-ip)
				ip="$2"
				shift;;

			-interactive) 
				interactive=1;;
				
			-help) 
				help=1;;
			
			--) shift
				break;;
				
			*)
			break;;
		esac
	shift
done

if [ "$help" = "1" ]; then
	help_console
	exit_program
elif [ "$interactive" = "1" ]; then
	interactiveMode
else
	if [ "$#" = "2" ]; then
		FILE=$1
		code=$2
		checkFile
	elif [ "$#" = "1" ]; then
		FILE=$1
		checkFile
	else
		printf "Запустить интерактивный режим прямо сейчас? [\e[1;32mY\e[0m/(a)] "
		read interactive
		if [ "$interactive" = "Y" -o "$interactive" = "y"  -o "$interactive" = "да"  -o "$interactive" = "Да"  -o "$interactive" = "Yes"  -o "$interactive" = "yes" ]; then
				clear
				interactiveMode
			else
				exit_program
			fi
	fi
fi

sortAWK="-h"
if [ "$reverse" = "1" ]; then
	sortAWK="$sortAWK -r"
fi

awk -v rsize="$rsize" -v ip_filter="$ip" -v code="$code" -v count="$count" -v url="$url" -v protocol="$protocol" '
	BEGIN {
		perfect_iteration=0
		FULLSIZE_REQUEST=0
	}{
		IP=$1
		TIMESTAMP=substr($4,2)
		ISO=substr($5, 0, length($5) - 1)
		TYPE_REQUEST=substr($6,2)
		URL_REQUEST=$7
		HTTP_PROTOCOL=substr($8,1,length($8) - 1)
		HTTP_CODE=$9
		SIZE_REQUEST=$10
		if (substr($11,2,length($11) - 2) == "-") { 
			REFER_REQUEST="Запрос выполнялся напрямую, а не по ссылке с другого сайта (поле реферер - пустое)"
		} else {
			REFER_REQUEST="Запрос выполнялся с " $11
		}
		CLIENT=substr($12,2)
		OS=substr($13,2)
		if (IP != "" && TIMESTAMP != "") {
		check = 1
		if (int(code) && int(HTTP_CODE) != code) {
			check = 0
		}
		if (ip_filter != 0 && IP != ip_filter) {
			check = 0
		}
		if (url != 0 && substr($11,2,length($11) - 2) != url) {
			check = 0
		}
		if (protocol != 0 && HTTP_PROTOCOL != protocol) {
			check = 0
		}

		if (check) {
			print TIMESTAMP " " ISO " с хоста " IP " по протоколу " HTTP_PROTOCOL " был выполнен запрос типа " TYPE_REQUEST " для получения ресурса находящегося по ссылке " URL_REQUEST ". Код ответа на запрос от сервера: " HTTP_CODE ". Такой ответ не предполагает наличия тела ответа (количество переданных байт - " SIZE_REQUEST, "). " REFER_REQUEST ". Клиент использовал для обращения программу " CLIENT ", ОС клиента: " OS
			perfect_iteration += 1
			FULLSIZE_REQUEST += SIZE_REQUEST
		}
		}
	} END {
		if (count == 1) {
			print "Выведено строк: " perfect_iteration
		}
		if (rsize == 1) {
			print "Колличество байт для данных строк: " FULLSIZE_REQUEST
		}
	}' "$FILE" | sort $sortAWK
	
exit_program