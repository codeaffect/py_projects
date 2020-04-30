import sys
import os
from github import Github

#token = '71a9aae88340b1e8ac4cf7ad6d3e076374d3af1a'

# for a in os.environ:
#     print('Var: ', a, 'Value: ', os.getenv(a))

# get folder name from parameters
folder_name = sys.argv[1]
# get git token from env vars
token = os.environ.get('gittoken')
print('folder name: %s' % folder_name)
print('token: %s' % token)

if len(folder_name) == 0 or len(token) == 0:
    print('>>>>>>>>> invalid token/foldername <<<<<<<')
    exit

# set variables
path = "c:/github/"
_dir = path + folder_name

if os.path.exists(_dir):
    print('>>>>>>>>>>>>>> git folder exists locally! <<<<<')
    exit

print(f'path: {_dir}')

# using git token
g = Github(token)

# get user info from github account
user_info = g.get_user()

# --- validate if folder is unique
repos = user_info.get_repos()
already_exists = folder_name in repos

if already_exists:
    print(' >>>>>> repo already exists! <<<<<<<')
    exit

exit
# create local folder
os.mkdir(_dir)

# get github login
login = user_info.login

print('login: %s' % login)

# set of git hub commands
# - git init, git remote add, git add, git commit, git push
commands = [f'echo "# {folder_name.upper()}" > README.md',
            f'cd {_dir}',
            f'echo {_dir}',
            'git init',
            f'git remote add origin git@github.com:{login}/{folder_name}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

print('** Creating repo .......')

for c in commands:
    os.system(c)

print('%s created locally' % folder_name)
os.system('code .')
