#!bin/bash

# Get the last commit message
last_commit_msg=$(git log --pretty=oneline | head -1 | cut -d' ' -f2-)

# Get the last commit description
last_commit_description=$(echo $last_commit_msg | cut -d':' -f2)

# Make switch statement case insensitive
shopt -s nocasematch
# Determine the commit type for inserting it into the changelog
case $last_commit_description in 

    *"Add"*)
    change_type="Added";;

    *"Change"*)
    change_type="Change";;

    *"Deprecate"*)
    change_type="Deprecate";;

    *"Remove"*)
    change_type="Removed";;

    *"Fix"*)
    change_type="Fixed";;

    *"Security"*)
    change_type="Security";;

esac

#Get the latest version from the changelog
last_version=$(cat ../CHANGELOG.md | grep -i -E -o "[0-9]+\.[0-9]+\.[0-9]+")	

# Read every part of the version into variables
IFS=. read -r major_old minor_old patch_old <<< "$last_version"

# Match the type of the conventional commit to a semantic version change and bump version
case $last_commit_msg in

    *"!"*)
    # increment
    major_new=$((major_old + 1))     
    new_version_num=$(echo "$major_new.0.0");;

    *"fix"*)
    # increment
    patch_new=$((patch_old + 1))
    new_version_num=$(echo "$major_old.$minor_old.$patch_new");;
    
    *"feat"*)
    # increment
    minor_new=$((minor_old + 1))
    new_version_num=$(echo "$major_old.$minor_new.0");;    

    *)
    echo "No semantic Versioning commit type found. Not updating the ChangeLog.";;

esac

# Update Changelog, insert the newest entry at the top of the file
echo -e "## [$new_version_num] - $(date +"%Y-%m-%d")\n### $change_type\n- $last_commit_description\n\n$(cat ../CHANGELOG.md)" > ../CHANGELOG.md