from github import Github

g = Github("codeaffect", "Sultry123")

g = Github("04509264f242a591d39a20299b5a47aeb7fe319a$")

for repo in g.get_user().get_repos():
    print(repo.name)
