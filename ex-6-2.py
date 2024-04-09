#!/usr/bin/env python3

jira_issues = {
    "PROJ-87": {"status": "In Progress", "summary": "Random Thing", "label": "test1"},
    "PROJ-12": {"status": "In Progress", "summary": "Random Thing", "label": "test2"},
    "PROJ-176": {"status": "ToDo", "summary": "Random Thing", "label": "test3"},
    "PROJ-986": {"status": "Closed", "summary": "Random Thing", "label": "test3"},
    "PROJ-614": {"status": "In Progress", "summary": "Random Thing", "label": "test6"},
    "PROJ-165": {"status": "Closed", "summary": "Random Thing", "label": "test1"},
    "PROJ-268": {"status": "In Progress", "summary": "Random Thing", "label": "test1"},
    "PROJ-999": {"status": "Closed", "summary": "Random Thing", "label": "test1"},
    "PROJ-845": {"status": "In Progress", "summary": "Random Thing", "label": "test2"},
    "PROJ-299": {"status": "In Progress", "summary": "Random Thing", "label": "test1"},
    "PROJ-642": {"status": "ToDo", "summary": "Random Thing", "label": "test1"},
    "PROJ-552": {"status": "Closed", "summary": "Random Thing", "label": "test2"},
    "PROJ-981": {"status": "In Progress", "summary": "Random Thing", "label": "test1"},
    "PROJ-111": {"status": "Closed", "summary": "Random Thing", "label": "test1"},
}

def show_issue(key, xyz):
    if xyz['status'] == "Closed" and xyz["label"] == "test1":
        print(key)


for cur_issue, issue_details in jira_issues.items():
    #print(cur_issue)
    show_issue(cur_issue, issue_details)