#!/bin/bash

git add .
git commit -m $1
git push origin main

echo "successfully pushed"