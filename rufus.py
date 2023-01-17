import git
import sys

n = sys.argv[1]
# Path to my repo: ~/Documents/Code/Rufus/
repo = git.Repo(n)
print(repo.index.diff(None))
print(repo.git.status())