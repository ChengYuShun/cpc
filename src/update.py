from .history import HOME_PATH
import os
import git
import time
import threading

VERSION = ''
flags = {}

with open(os.path.join(HOME_PATH, 'VERSION'), 'r') as f:
    VERSION = f.read().strip()


def check_update(repo: git.Repo, remote: git.Remote):
    remote.fetch()
    local_branch = repo.active_branch
    remote_branch = repo.remotes.origin.refs[local_branch.name]
    return local_branch.commit != remote_branch.commit


def animation(msg, count):
    n = 0
    while flags[msg]:
        n += 1
        print(msg + '.' * n + ' ' * (count - n), end='\r')
        n %= count
        time.sleep(.5)

def new_animation(msg, count, work, *args, **kwargs):
    flags[msg] = True
    threading.Thread(target=animation, args=(msg, count)).start()
    result = work(*args, **kwargs)
    flags[msg] = False
    return result


def update():
    repo = git.Repo(HOME_PATH)
    remote = repo.remote()

    if new_animation('Checking Update', 3, check_update, repo=repo, remote=remote):
        # 询问是否更新
        u = input('There is a new version of the program. Do you want to update it? [y/N] ').strip().lower()
        if u == 'y':
            try:
                new_animation('Updating', 3, remote.pull)
                print('\033[1mUpdate Successful\033[0m')
            except Exception as e:
                print(f'\033[1;31mFailed to Update\033[0m\n\t{e}')
        else:
            print('Stop Updating')
    else:
        print('You are using the latest version!')