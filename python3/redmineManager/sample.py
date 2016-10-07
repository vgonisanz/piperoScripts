# Usage:
# Dependencies: sudo pip3.4 install python-redmine
# Also need: Redmine server
import sys
import os

from redmineManager import RedmineManager

# Inputs
redmine_url = 'http://test.com/redmine/'
redmine_user_id = '999999999999999999999999999999999999999' 	# User ID
redmine_project_name = 'test_project'

# Global variables
scriptname = ""
pathname = ""
full_path_name = ""
input_path = ""
output_path = ""
parser = None
redmine_manager = None

# Sample functions
#############################################################
def abort_exe( exit_message ):
    print(exit_message)
    print("Aborting...")
    sys.exit(0)
    return

def initialize():
    scriptname = sys.argv[0]
    pathname = os.path.dirname(sys.argv[0])
    full_path_name = os.path.abspath(pathname)

    print("\n")
    print("==================================================================")
    print('   Executing: ', scriptname)
    print("==================================================================")
    print("\n")

    # Create output path if needed
    output_path = os.path.join(full_path_name, "output/")
    if not os.path.exists(output_path):
        print("Creating output path...")
        os.makedirs(output_path)

    print("Creating input and output path...")
    input_path = os.path.join(full_path_name, "input")
    output_path = os.path.join(full_path_name, "output")
    print("Input: %s" % input_path)
    print("Output: %s" % output_path)
    return

def try_initialize_redmine():
    print("Initializing redmine...")
    redmine_manager = RedmineManager(redmine_url, redmine_user_id, redmine_project_name)
    successful = redmine_manager.connect_redmine()
    if successful == False:
        abort_exe("Error connection Redmine")
    redmine_manager.get_all_redmine_issues()
    return

def try_update_redmine(array_data):
    print("Using array data to update redmine....\n")
    for data in array_data:
        issueID = data['Issue']
        del data['Issue']
        issue = redmine_manager.read_redmine_issue_by_id(issueID)
        redmine_manager.update_issue_with_array(issue, data, False)
        redmine_manager.save_issue(issue)
        print("\n")
    print("Done.")

def create_values():
    print("Creating test values...")
    array_data = []
    data = {}
    data["Issue"] = 1
    data["Title"] = "Title 1"
    data["Descriptions"] = "This is the description for issue 1"
    array_data.append(data)
    data2 = {}
    data2["Issue"] = 2
    data2["Title"] = "Title 2"
    data2["Descriptions"] = "This is the description for issue 2"
    array_data.append(data2)
    print("Using data: %s" % array_data)
    return array_data

if __name__ == '__main__':
    # Initialize
    ###########################################################
    initialize()
    #try_initialize_redmine()

    # Use class
    ###########################################################
    array_data = create_values()
    #try_create_redmine_project(array_data) # Working on server test
    #try_update_redmine(array_data)

    print("\n")
    print("==================================================================")
    print("   Finish.")
    print("==================================================================")
    print("\n")
