from jsonManager import JsonManager
import sys
import os

def abort_exe( exit_message ):
    print(exit_message)
    print("Aborting...")
    sys.exit(0)
    return

def process_key(self, key, newvalue):
    print("Changing key: %s with value: %s" % (key, newvalue))

def testinfo(self):
    print("testinfo")

if __name__ == '__main__':
    # Configure variables to provide to class
    #############################################################
    jsonkeys = ['a', 'b', 'd']
    input_path = os.path.join(os.getcwd(), "input/")

    # Use class
    ###########################################################
    # Create instance
    parser = JsonManager('parser')
    # Set array with keys
    parser.set_key_array(jsonkeys)
    # Set input path
    parser.set_input_path(input_path)
    # Parse json file
    successful, json_data = parser.read_json_from_file("test.json")
    print("successful? %s" % successful)

    # Get a value if exist or print error
    #value = parser.get_value(json_data, 'f')
    #print("Value is: %s" % value)
    # Print and get a value
    #value = parser.print_json_value(json_data, 'a')
    # Print all json values
    #parser.print_all_json_values(json_data)
    # Print only values in array
    #parser.print_arraykey_json_values(json_data, jsonkeys)
    # Process default
    parser.process_function()
    # Overload processing with function
    parser.set_process_function(process_key)
    # Call new process function
    #parser.process_function("key", "value")


    # Try to parse wrong file
    #successful, json_data = parser.read_json_from_file("wrong_file.json")
    #print("successful? %s" % successful)

    # parser.test()
    #abort_exe("Finish.")
