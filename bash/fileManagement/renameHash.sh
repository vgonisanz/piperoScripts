#!/bin/bash
# ================================================================================
# Author:   vgonisanz
# Date:     2016
# ================================================================================
# Template to make scripts with option easier.
# Check spell http://www.shellcheck.net/  # online, or download, to test!

# Global variable declaration
# ================================================================================
outputpath="$(pwd)/output"               # Output folder by default
inputpath="$(pwd)/input"                 # input folder by default

# Function declaration
# ================================================================================
### OPTIONS
# This function, display usage info
f_display_usage()
{
  echo -e "\n--------------------------------------------------"
	echo "|  This function teach you how this script works"
	echo -e "|  Usage:\n|  $0"  # -e option allow use \n
  echo "|  ${optionHelp} = Print usage"
  echo "|  ${optionInput} = Set input path"
  echo "|  ${optionOutput} = Set output path"
  echo -e "--------------------------------------------------"
}
f_get_hash()
{
  #temp=$(echo "${1}" | sed 's/\-/ /' )
  #temp=`md5sum ${1} | awk '{ print $1 }'`
  echo ${temp}
}
f_process()
{
  echo -e "Renaming files from: \n ${inputpath}\n to:\n ${outputpath}"
  if [ ! -d "${outputpath}" ] # d for directory
  then
    echo "  Creating output folder..."
    mkdir ${outputpath}
  fi
  echo -e "Processing..."
  counter=0
  for file in "${inputpath}"/*    # * = All items, in output path
  do
      outfile=$(f_get_hash "${outfile}")
      echo "  Filename ${counter}: ${file##*/} --> ${outfile}"
      cp "${file}" "${outputpath}/${outfile}"
      let "counter += 1"  # Forward
  done
  echo "  ${counter} files processed! All files copied in output"
  echo -e "done!"
}

### Other functions
# Check if are provided correct arguments
f_evaluate_options()
{
  echo "  Evaluation options, number of arguments: ${Nargs}"
  eval set -- ${options}
  echo "  Options: ${options}"
}
# End Function declaration
##################################################################################

# Main program
# ================================================================================

# First of all, store arguments in a variable.
# Bash have variable when call an executable, $0 = CommandName, $1..$N = Arguments
# We store arguments in an array. If a function is called, you cannot access to them if not are global variables
# because they are overwrited by function arguments.
args=(${@}) # Arguments
Nargs=(${#})  # Number of arguments

# We define options, using getopt
# -o Each single character stands for an option
# -l Long name for each option
# : after an option (short or long) tells that option is required argument
# :: tells is a optional argument
# For extension take a look here: http://www.bahmanm.com/blogs/command-line-options-how-to-parse-in-bash-using-getopt
options=$(getopt -o hi:o: -l help,input:,output: -- "${@}")
if [[ $? -ne 0 ]]
then
  echo "  Error: Detected invalid option"
fi
# -o hs:ao = h & a option, no arguments; s option with a required option;
# -l help,say:,author = same.
# Declarate variables with options to clarify
optionHelp="-h|--help"
optionInput="-i|--input"
optionOutput="-o|--output"

# We define some global variables
commandName=$(basename "$0")        # Extract name from first variable
commandPath=$(pwd)                  # Get the path with command pwd

# Call a function to evaluate arguments as options
f_evaluate_options

# Check all arguments
# We are going to check the all the options shifting them.
# Using shift, the positional parameters are shifted to the left by this number, N.
# Using case syntaxis, more info: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html
while [ "$1" != "" ]
do
  case "$1" in
      -h|--help) f_display_usage ;; # Call function
      -i|--input) inputpath=${2} ; echo "   Setting Input path: ${2}" ; shift ;; # Call function, reading next variable and shift
      -o|--output) outputpath=${2} ; echo "   Setting Output path: ${2}" ; shift ;; # Call function, reading next variable and shift
      *)         echo "Unknown option: $1" ; f_display_usage ; break ;;
  esac
  shift;  # Advance
done;
# Last step, process all files with input and output
f_process
