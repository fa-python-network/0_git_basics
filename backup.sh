#!/bin/bash

/usr/bin/rclone copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/home/sbochkarev/Documents" "gdrive:work-computer"
