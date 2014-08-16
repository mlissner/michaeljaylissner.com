Title: Script to Clean Up F-Spot Database
Date: 2009-10-14T00:30:12
Tags: sqlite3, f-spot, database, bash


One of the more popular photo management applications for Linux is f-spot, but unfortunately it has a rather glaring bug. It uses a sqlite3 database internally to track which pictures you've imported into it, what tags they have, etc. However, if you delete, move or rename any of the files that f-spot is tracking, the next time you browse to that photo within f-spot, it will crash the program. It's annoying, and there's no particularly easy way to deal with it...until now.

The script below (and attached) simply iterates through all of the photos that are in f-spot's database, and checks to see if those photos exist on your hard drive. If you run it in demo-mode, it will show you which files look problematic, and if you run it in normal mode, it will delete those database entries so that your database is cleaned up (but not before backing up your database, just in case).

In my very limited testing, it works very well, any additional feedback or bug reporting is more than welcome. 
<code lang="text">#!/bin/bash

# A script to find missing files in the f-spot database, and then delete them.
# At present these files crash f-spot. It's frustrating as all hell.

echo "Welcome to the f-spot database cleaner. All the usual disclaimers apply, as you might imagine."
echo "What would you like to do: " 
echo "  1) Run in demo-mode " 
echo "  2) Clean up your f-spot database" 
echo "  3) Quit" 
read -p "Your choice: " choice

case $choice in 
    1) demomode="true";;
    2) demomode="false";;
    3) exit 0;;
esac

# With that beginning stuff out of the way, let us do some functions
# First, a function to gather the database contents and to print out the ones that are orphans

function findAndFixOrphans {
    # find our db, and set a var. Checking for XDG path first, since it's the more recent location of the db
    if [ -f $XDG_CONFIG_DIR/f-spot/photos.db ] #checks if the $XDG_CONFIG_DIR variable is in use
    then
        DBPATH=$XDG_CONFIG_DIR/f-spot/photos.db
    elif [ -f $HOME/.config/f-spot/photos.db ] #uses the default $XDG location, if that's being used.
    then
        DBPATH=$HOME/.config/f-spot/photos.db
    elif [ -f $HOME/.gnome2/f-spot/photos.db ] #uses the old location of the DB, if the former aren't in use.
    then
        DBPATH=$HOME/.gnome2/f-spot/photos.db
    else
        echo "Error: Could not find database. Damn." 
        exit 1
    fi

    # Select the filenames, and put them in a variable.
    filenames=$(sqlite3 $DBPATH "SELECT URI FROM PHOTOS")
    filenames_versions=$(sqlite3 $DBPATH "SELECT URI FROM PHOTO_VERSIONS")

    # Chomp off the first instance of file://, and replace the rest with newlines.
    filenames=$(echo $filenames | sed 's/file:\/\///' | sed 's/file:\/\//\n/g'  )
    filenames_versions=$(echo $filenames_versions | sed 's/file:\/\///' | sed 's/file:\/\//\n/g' )

    if [ $demomode == "true" ]
    then            
        while read -r line
        do
            # Decode the filename
            decodedLine=$(echo -e "${line//\%/\\x}")
            if [ ! -f  "$decodedLine" ] 
            then
                # If the file doesn't exist, we output the filename, if in demomode, or we fix it if we are not in demomode.
                echo  "Errant record found in the photos table: $decodedLine"
            fi
        done <<< "$filenames"
        
        # We do the same for the photo_versions table
        while read -r line
        do
            # Decode filename
            decodedLine=$(echo -e "${line//\%/\\x}")
            if [ ! -f "$decodedLine" ]
            then
                # If the file doesn't exist, we output the filename
                echo "Errant record found in the photo_versions table: $decodedLine"
            fi
        done <<< "$filenames_versions"

    else
        # We backup the database, and make the correction
        cp $DBPATH $DBPATH.`date -I`.bak
        if [ $? -eq 0 ]
        then
            #The backup worked, tell the user.
            echo "Your database has been backed up to $DBPATH.`date -I`.bak"
        else
            echo "Error backing up your database."
            exit 3
        fi
        
        # First we do the photos table
        while read -r line
        do
            # Decode the filename
            decodedLine=$(echo -e "${line//\%/\\x}")
            
            if [ ! -f "$decodedLine" ]
            then
                # Do some sql here.
                foo="file://${line}"
                echo -n "Deleting URI $line from the database table photos..."
                sqlite3 $DBPATH "DELETE FROM PHOTOS WHERE uri = '$foo'"
                echo "done."
            fi
        done <<< "$filenames"

        # Then we do the photo_versions table
        while read -r line
        do
            # Decode the filename
            decodedLine=$(echo -e "${line//\%/\\x}")

            if [ ! -f "$decodedLine" ]
            then
                #Do some sql stuff
                foo="file://${line}"
                echo -n "Deleting URI $line from the database table photo_versions..."
                sqlite3 $DBPATH "DELETE FROM PHOTO_VERSIONS WHERE uri = '$foo'"
                echo "done."
            fi
        done <<< "$filenames_versions"

    fi

}

if [ "$demomode" == "true" ]
then
    echo "Great. Proceeding in demomode."
    
    findAndFixOrphans

    echo "Demomode successfully finished. Exiting."
    exit 0;
elif [ "$demomode" == "false" ]
then
    echo "Great. Cleaning up your database."
    
    findAndFixOrphans    

    echo "Database cleaned successfully."
    exit 0;
else
    echo "Something strange happened. See the script for details. Exiting."
    exit 2;
fi
</code>