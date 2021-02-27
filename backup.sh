#!/bin/bash
echo $USER
echo $HOME
echo "Initializing backup..."
tar -czvf $USER.tar.gz $HOME
