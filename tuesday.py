#!/usr/bin/env python3

#Read file: jira-issues.txt
#Print all of the issues as:
#“Project: PROJ and number: 123”


fp = open("jira-issues.txt")

contents = fp.read()
# aaa-a-a-aaaaa-aaa
#print(dir(contents))
print(contents.split("\n"))
jira_issues = contents.split("\n")
for cur in jira_issues:
    if cur == '':
        continue
    parts = cur.split("-")
    #print(parts)
    project_name = parts[0]
    issue_number = parts[1]
    #project_name = cur[:5]
    #issue_number = int(cur[6:])
    print("Project: {0} and number: {1}".format(project_name, issue_number))
#print(contents)


fp.close()