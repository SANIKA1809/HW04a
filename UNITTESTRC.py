import Repocommit

def test_get_repo_commits():
    username = "SANIKA1809"
    repo_commits = Repocommit.get_repo_commits(username)
    assert isinstance(repo_commits, dict)
    assert len(repo_commits) > 0
    assert all(isinstance(key, str) for key in repo_commits.keys())
    assert all(isinstance(value, int) for value in repo_commits.values())
