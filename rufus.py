import git
import sys

git_dir = sys.argv[1]

# Path to my repo: ~/Documents/Code/Rufus/
repo = git.Repo(git_dir)
g = git.Git(git_dir)
active_branch = repo.active_branch
reader = repo.config_reader()

print(f"active branch: {active_branch.name}")
print(f"local files: {repo.is_dirty()}")
remote = repo.remote('origin')
remote.fetch()
latest_remote_commit = remote.refs[repo.active_branch.name].commit
latest_local_commit = repo.head.commit

print(f"recent commit: {latest_local_commit == latest_remote_commit}")
commits_list = list(repo.iter_commits())
for i in range(1):
    commit = commits_list[i]
    author = repo.git.show("-s","--format=Author: %an", commit.hexsha)
    print(f"blame Rufus: {author == 'Rufus'}")
