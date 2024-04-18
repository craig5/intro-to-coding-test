#!/usr/bin/env python3

class JiraIssue:

    def __init__(self, issue_key):
        self.issue_key = issue_key

    def print(self):
        parts = self.issue_key.split("-")
        if len(parts) != 2:
            print("ERROR: Incorrect format for issue key.")
            return
        project = parts[0]
        number = parts[1]
        print("Project: {}  Number: {}".format(project, number))

issue_1 = JiraIssue("RANDOM-99")
issue_1.print()

issue_2 = JiraIssue("FOO-BAR-11")
issue_2.print()

bad = JiraIssue("FOO55")
bad.print()
