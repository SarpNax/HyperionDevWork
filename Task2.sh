#!/bin/bash
#for linux 
echo "lets get upgrading"
#this is to remove any excess packages
apt autoremove
#updating systems 
apt update
#to proceed with update
echo "y"
#updates the operating system (Linux)
apt upgrade