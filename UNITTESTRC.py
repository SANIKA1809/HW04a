# import necessary modules
import unittest

# define the function
def get_user_repos_with_commits(user_id):
    # your code here
    pass

# define the test class
class TestGitHubAPI(unittest.TestCase):

    def test_get_user_repos_with_commits(self):
        # call the function
        user_id = "SANIKA1809"
        repos = get_user_repos_with_commits(user_id)
        # assertions here
        self.assertIsInstance(repos, list)
        for repo in repos:
            self.assertIn("name", repo)
            self.assertIn("commits", repo)
            self.assertIsInstance(repo["name"], str)
            self.assertIsInstance(repo["commits"], int)