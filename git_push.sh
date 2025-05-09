#!/bin/bash

# Automated code for git push
echo "Pushing to git:"

COMMIT=$(date +"%Y%m%d-%H%M%S")
#read -p "commit name: " COMMIT

# Add all changes
git add -A
# Commit changes with a message
git commit -m "$COMMIT"

# Push changes to the remote repository
git push

# End message
echo "done"


#####################################
## NOTES:
## 1) always create new repo from github following their instructions
## 2) Above script for regular pushes
## 3) If not working, probably password expired:
## - make new password (token) on github (attach extra rights to edit/overwrite)
##)- update password locally by entering:
# git config --global credential.helper store 
## and then making a manual push entering username and password


