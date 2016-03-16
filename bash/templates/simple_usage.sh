#!/bin/bash
# ================================================================================
# Author:   vgonisanz
# Date:     2016
# ================================================================================
# Template to make scripts with option easier.
# Check spell http://www.shellcheck.net/  # online, or download, to test!

# Global variable declaration
# ================================================================================
# No needed

# Function declaration
# ================================================================================
### OPTIONS
# This function, display usage info
f_display_usage()
{
	echo -e "  · Usage for: $0 -p [print]";
	echo -e "  · [print] = Message to print";
	exit 1;
}
f_print()
{
	echo -e "Print message: ${1}"
}
# End Function declaration
##################################################################################

# Main program
# ================================================================================ 
# Call usage if no args
[[ $# -eq 0 ]] && f_display_usage

# Check all arguments
# We are going to check the all the options shifting them.
echo -e "Processing..."
while [ "$1" != "" ]
do
  case "$1" in
      -h|--help) 
	f_display_usage ;; 	# Call usage if help
      -p|--print)
	f_print ${2} ; shift ;;		# Call to print with next arg as variable
      *)         
	echo "Unknown option: $1" ; f_display_usage ; break ;; # Usage if no valid option
  esac
  shift;  # Advance
done;
echo -e "done."
