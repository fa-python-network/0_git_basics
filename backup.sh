#!/bin/bash
I1=$(echo $(whoami) ~)
I2=$(($(echo $(whoami) | wc -m)-1 + $(echo ~ | wc -m) - 1))
echo $I1
