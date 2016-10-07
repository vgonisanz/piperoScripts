from redmine import Redmine

"""
This python 3 class will manager redmine for you.

To generate HTML documentation for this module issue the command:

    pydoc -w jsonManager

"""
class RedmineManager(object):
    _redmine_url = ''
    _redmine_user_id = ''
    _redmine_project_name = ''
    _connection = ''
    _redmine_handler = None
    _project_handler = None
    _issues = None

    """
    Initialize RedmineManager with redmine URL, a developer id to identify each petition, and project to work.
    """
    def __init__(self, redmine_url, user_id, project_name):
        """
        Construct a new 'RedmineManager' object.

        :param redmine_url: Redmine URL.
        :param user_id: User valid ID to authorize petitions.
        :param project_name: Current file in write mode to save json.
        :return: returns nothing
        """
        self._redmine_url = redmine_url
        self._redmine_user_id = user_id
        self._redmine_project_name = project_name
        return

    """
    Connect to redmine.
    """
    def connect_redmine(self):
        successful = False
        print("Connecting to redmine...")
        self._redmine_handler = Redmine(self._redmine_url, key=self._redmine_user_id)
        self._project_handler = self._redmine_handler.project.get(self._redmine_project_name)
        if (self._redmine_handler != None and self._project_handler != None):
            successful = True
        return successful

    """
    Get in memory all redmine issues
    """
    def get_all_redmine_issues(self):
        print("Getting all redmine issues")
        self._issues = self._redmine_handler.issue.all()
        return

    """
    Get a issue using its ID
    """
    def read_redmine_issue_by_id(self, issueID):
        print("Reading redmine issue: %s" % issueID)
        # try to get issue
        issue = self._redmine_handler.issue.get(issueID)
        return issue

    """
    Update issue with array values
    """
    def update_issue_with_array(self, issue, array_values, print_values=False, print_warnings=True):
        print("Trying to update issue %s" % (issue.id) )
        if print_values == True:
            print("Using values: %s" % array_values)
        issue_custom_values = list(issue.custom_fields.values())
        for value in array_values:
            updated = False
            for custom_value in issue_custom_values:
                if custom_value['name'] == value:
                    custom_value['value'] = array_values[value]
                    updated = True
            if updated == False:
                if print_warnings == True:
                    print("Warning, value: %s not found on issue" % value)
            else:
                if print_values == True:
                    print("Updated value: %s" % value)
        issue.custom_fields = issue_custom_values
        return

    """
    Save issue with content
    """
    def save_issue(self, issue):
        result = issue.save()
        if result:
            print("Saved issue: %s succesfully" % issue.id)
        else:
            print("Error saving issue: " % issue.id)

    """
    Print issue info
    """
    def print_issue_info(self, issue):
        print("id: %s" % issue.id)
        print("author: %s" % issue.author)
        print("assigned_to: %s" % issue.assigned_to)
        print("description: %s" % issue.description)
        print("status: %s" % issue.status)
        print("created_on: %s" % issue.created_on)
        print("updated_on: %s" % issue.updated_on)
        issue_custom_values = list(issue.custom_fields.values())
        for custom_value in issue_custom_values:
            print(value)
