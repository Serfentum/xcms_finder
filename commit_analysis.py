from init_repo import init_repo


def find_commit(repo, local_repo, version, branch='master'):
    """
    Find commit with specified version in the DESCRIPTION file in the xcms repo
    This function checkout to specified version
    :param repo: git.repo.base.Repo - repository object
    :param local_repo: str - path to the local repository
    :param version: str - necessary version
    :param branch: str - in which branch to search
    :return: str - necessary commit sha
    """
    # Description file path
    description_path = local_repo / 'DESCRIPTION'
    
    # Find commit with desired version in DESCRIPTION file
    for commit in repo.iter_commits(branch):
        # Checkout previous version
        repo.git.checkout(commit)
        
        # Inspect DESCRIPTION in the previous commit
        with open(description_path) as description:
            description.readline()
            description = description.readline().strip()
            description = description.split(': ')[1]
            print(description)
            
        # Stop if we found commit with desired version
        if description == version:
            sha = commit.hexsha
            print(f'version {version} was found in the {sha} commit')
            print('try to build it in the correspondent image')
            return sha
        
    raise ValueError(f'{version} was not found')
    

if __name__ == '__main__':
    version = '3.0.0'
    path = '~/skoltech/aspire/server/different_xcms'

    # Load from github
    repo_clone_url = 'https://github.com/sneumann/xcms.git'

    repo, local_repo = init_repo(repo_clone_url=repo_clone_url,
                                 path=path,
                                 version=version)

    find_commit(repo=repo,
                local_repo=local_repo,
                version=version,
                branch='master')
