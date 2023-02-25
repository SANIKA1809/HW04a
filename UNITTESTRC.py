import requests
import json
import unittest

class TestGitHubAPI(unittest.TestCase):
    
    def test_number_of_commits(self):
        response = requests.get('https://api.github.com/users/SANIKA1809/repos')
        data = json.loads(response.text)

        for repo in data:
            commits_url = repo['commits_url'].replace('{/sha}', '')
            commits_response = requests.get(commits_url)
            commits_data = json.loads(commits_response.text)
            num_commits = len(commits_data)
            
            self.assertTrue(num_commits >= 0)
