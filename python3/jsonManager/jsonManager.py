import os
import json
import csv
import collections
import pathlib

"""
This python 3 class will manager json individually for you.

To generate HTML documentation for this module issue the command:

    pydoc -w jsonManager

"""

class JsonManager(object):
    _name = None
    _key_array = [None] * 0
    _json_data = json.dumps({})
    _input_path = "input/"
    _output_path = "output/"
    _current_filename = "None"
    _function_callback = None

    """
    Initialize JsonManager with a name to identify eash instance
    """
    def __init__(self, name):
        """
        Construct a new 'JsonManager' object.

        :param current_json: Current json data readed in memory.
        :param current_read_file: Current file with a valid json.
        :param current_write_file: Current file in write mode to save json.
        :return: returns nothing
        """
        self._name = name

    """
    Print parser ID
    """
    def print_ID(self):
        """
        Prints json Manager ID to the display.
        """
        print(self._name)
        return

    """
    Test function
    """
    def test(self):
        print("Name: %s" % self._name)
        print("Input file: %s" % self._input_path)
        return

    """
    set_key_array
    """
    def set_key_array(self, key_array=_key_array):
        print("Setting keys: %s" % list(key_array) )
        _key_array = key_array
        return

    """
    set_input_path
    """
    def set_input_path(self, input_path=None):
        if input_path is None:
            input_path = self.input_path
        print("Setting input path: %s" % input_path)
        self._input_path = input_path
        return

    """
    set_output_path
    """
    def set_output_path(self, output_path=None):
        if output_path is None:
            output_path = self.output_path
        print("Setting output path: %s" % output_path)
        self._output_path = output_path
        return

    """
    set_process_function
    """
    def set_process_function(self, function_callback=None):
        #if function_callback is None:
        #    function_callback = self.process
        print("Setting process function: %s" % function_callback)
        self._function_callback = function_callback
        return

    """
    process_function_default
    """
    def process_function(self, arguments=None):
        if(self._function_callback == None):
            print("Default process... overload call with set_process_function!")
        else:
            self._function_callback(arguments)
        return

    """
    print_json_value
    """
    def print_json_value(self, json_data=None, key=None):
        value = None
        if json_data is None:
            json_data = self._json_data
        if(key in json_data):
            value = json_data[key]
            print("Value is: %s" % value)
        else:
            print("Missing value: %s in json" % key)
        return value

    """
    print_all_json_values
    """
    def print_all_json_values(self, json_data=None):
        if json_data is None:
            json_data = self._json_data
        print("Json contains keys: %s" % list(json_data))
        for key, value in json_data.items():
            print("Key: %s with value: %s" % (key, value))
        return

    """
    print_arraykey_json_values
    """
    def print_arraykey_json_values(self, json_data=None, array_key=None):
        if json_data is None:
            json_data = self._json_data
        if array_key is None:
            array_key = self._array_key
        print("Json read only keys: %s" % list(array_key))
        for key in array_key:
            value = json_data[key]
            print("Key: %s with value: %s" % (key, value))
        return

    """
    Read json
    :return: successful
    :return: _json_data data in json
    """
    def read_json_from_file(self, file_name=None):
        successful = False
        json_data = json.dumps({})
        if file_name is None:
            return successful, json_data
        print("Reading file: %s" % file_name)
        full_source_name = os.path.join(self._input_path, file_name)
        if(pathlib.Path(full_source_name).is_file()):
            with open(full_source_name) as data_file:
                self._json_data = json.load(data_file, object_pairs_hook=collections.OrderedDict)
                successful = True
        else:
            print("File: %s no exist." % file_name)
        return (successful, self._json_data)

    """
    Write json
    """
    def write_json(self, file_name, json_data):
        print("Writing: %s" % file_name)
        full_destination_name = os.path.join(self._output_path, file_name)
        with open(full_destination_name, 'w') as outfile:
            json.dump(json_data, outfile)
        return

    """
    Get value from json
    """
    def get_value(self, json_data=None, key=None):
        value = None
        if json_data is None:
            json_data = self._json_data
        if(key in json_data):
            value = json_data[key]
        else:
            print("Missing value: %s in json" % key)
        return value

    """
    create_json_object_from_list
    """
    def create_json_object_from_list(self, list_of_list=None):
        successful = True
        data = {}
        for pair in list_of_list:
            data[pair[0]] = pair[1]

        return successful, data
