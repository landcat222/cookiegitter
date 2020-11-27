#!/bin/sh
cd $1
git init
git add *
git commit -m "Initial commit"
hub create
git push -u origin main
