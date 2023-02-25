# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:21:52 2023

@author: Sanika More
"""

import requests
import json

# make a request to the GitHub API
response = requests.get('https://api.github.com/users/SANIKA1809/repos')

# parse the response data as JSON
data = json.loads(response.text)

# iterate over each repository and get the number of commits
for repo in data:
    commits_url = repo['commits_url'].replace('{/sha}', '')
    commits_response = requests.get(commits_url)
    commits_data = json.loads(commits_response.text)
    num_commits = len(commits_data)
    print(repo['name'], num_commits)
