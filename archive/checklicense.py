#!/usr/bin/env python
# This is a hook that will check whether a file has a license or not. If it 
# lacks the license, then it will add the information found in license.txt

def check_license(filename):
    # This method will simply check if the license is there. If found, it does 
    # nothing. If not, it will hand off the file to the add_license method.
    
    # Open the file, and add its contents to a string
    file_to_check = open(filename, 'r')
    file_contents = file_to_check.read()
    
    # check if the file contains the terms. User lowercase for good measure.
    if "affero general public license" not in file_contents.lower():
        file_to_check.close()
        add_license(filename)


def add_license(filename):
    # This method adds the license information found in license.txt to the 
    # file it is handed. This method will be called by check_license, if needed.

    file_to_fix  = open(filename, 'r')
    file_to_fix_contents = file_to_fix.read()

    # if it's a python file...
    if ".py" in filename:
        python_license_file = open('python_license.txt', 'r')
        python_license_text = python_license_file.read()
        new_contents = python_license_text + file_to_fix_contents

        # close the file as read, then open it as write, make the change, the close it again.
        file_to_fix.close()
        file_to_fix = open(filename, 'w')
        file_to_fix.write(new_contents)
        file_to_fix.close()

    # if it's a java file...
    elif ".java" in filename:
        java_license_file = open('java_license.txt', 'r')
        java_license_text = java_license_file.read()
        new_contents = java_license_text + file_to_fix_contents
        
        # This is the same pattern as above.
        file_to_fix.close()
        file_to_fix = open(filename, 'w')
        file_to_fix.write(new_contents)
        file_to_fix.close()

    # if it's neither, something has gone wrong. Throw an error and exit.
    else:
        print "Invalid file type: " + filename
        sys.exit(1)

    
    print "License information added to: " + filename




if __name__ == '__main__':
    import sys, os
    
    # Pipe the names of the files that have been modified or added into the for loop.
    # For each one, check if it's python or java, and if so, run the check_license method.
    for file in os.popen('hg st -n -a -m'):

        # We only do this for python and java files...at least for now.
        if (".py" in file) or (".java" in file):
            # We must strip the newline
            file = file.rstrip("\n")
            # print 'running check license on ' + file
            check_license(file)
