#!/bin/bash

# Путь к исходной директории для резервного копирования
source_dir="/path/to/source/directory"

# Путь к директории, в которой будет сохранена резервная копия
backup_dir="/path/to/backup/directory"

# Создание имени файла резервной копии с текущей датой и временем
timestamp=$(date +"%Y%m%d%H%M%S")
backup_file="backup_${timestamp}.tar.gz"

# Создание директории для резервной копии, если она не существует
mkdir -p "${backup_dir}"

# Создание архива резервной копии
tar -czf "${backup_dir}/${backup_file}" "${source_dir}"

# Проверка успешности создания архива
if [ $? -eq 0 ]; then
  echo "Резервная копия успешно создана: ${backup_dir}/${backup_file}"
else
  echo "Ошибка при создании резервной копии"
fi
