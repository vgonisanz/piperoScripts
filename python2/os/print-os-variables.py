# # Description: Just print some variables from O.S Interface 
# Reference: https://docs.python.org/2/library/os.html#process-parameters 

# Dependencies
import os

# Get variables
VAR_USER_NAME=os.getlogin()
VAR_SO=os.uname()
VAR_CURRENT_PATH=os.getcwd()
VAR_HOME_PATH=os.environ['HOME']

# Print all values
print '\nHi ' + VAR_USER_NAME + ' your variables are:' 
print 'S.O: ' + ' - '.join(VAR_SO)
print 'Current path: ' + VAR_CURRENT_PATH
print 'Home Path: ' + VAR_HOME_PATH
