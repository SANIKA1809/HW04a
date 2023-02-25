import unittest
from unittest.mock import MagicMock
import json

# import the code to be tested
import Repocommit

class TestMyCode(unittest.TestCase):

    def test_number_of_commits(self):

        # set up a mock response for the GitHub API request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "commits_url": "https://api.github.com/repos/SANIKA1809/repo1/commits{/sha}",
                "name": "repo1"
            },
            {
                "commits_url": "https://api.github.com/repos/SANIKA1809/repo2/commits{/sha}",
                "name": "repo2"
            }
        ]

        # set up a mock response for the commits API request
        mock_commits_response = MagicMock()
        mock_commits_response.status_code = 200
        mock_commits_response.json.return_value = [
            {
                "sha": "commit1",
                "commit": {
                    "message": "commit message 1"
                }
            },
            {
                "sha": "commit2",
                "commit": {
                    "message": "commit message 2"
                }
            }
        ]

        # patch the requests module to return the mock responses
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.side_effect = [mock_response, mock_commits_response]

            # call the function to be tested
            result = Repocommit.get_number_of_commits('https://api.github.com/users/SANIKA1809/repos')

            # assert the results
            expected_result = {'repo1': 2, 'repo2': 2}
            self.assertEqual(result, expected_result)
