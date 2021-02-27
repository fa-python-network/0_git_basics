#!/bin/bash
#this script creates an archived backup of the user's home folder
echo $USER
echo $HOME
echo "Initializing backup..."
tar -czvf $USER.tar.gz $HOME
