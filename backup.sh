: TODO world and auth backup
mysqldump -uroot -p characters > characters_dump.sql
mysqldump -uroot -p world > world_dump.sql
mysqldump -uroot -p auth > auth_dump.sql