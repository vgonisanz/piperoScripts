from configuration import *
import argparse

def print_configuration_vars():
   "This prints configuration variables"
   print "This prints configuration variables:"
   print "-------------------------------------"
   print "var_foo value is: " + var_foo
   print "var_var value is: " + var_var
   print "var_home value is: " + var_home
   return

parser = argparse.ArgumentParser(description="Load easy configuration")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
args = parser.parse_args()

if args.quiet:
    print "quiet = nothing to say"
elif args.verbose:
    print "\nThis sample talk a lot....\nOk, lets go\n"
    print_configuration_vars()
else:
    print_configuration_vars()
