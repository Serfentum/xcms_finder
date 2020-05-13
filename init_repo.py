from pathlib import Path

import git


def init_repo(repo_clone_url, path, version):
    """
    Clone repo from url to specified path, dir with it will be named as version
    :param repo_clone_url: str - url from gihub to clone
    :param path: str - path, where dir with repo will be places
    :param version: str - future name of repo dir
    :return: git.repo.base.Repo, str - repository object and path to the correspondent local repository
    """
    # Create path for repo
    local_repo = Path(path) / version
    local_repo = local_repo.expanduser()
    
    # Initialize repository
    repo = git.Repo.clone_from(repo_clone_url, local_repo)
    return repo, local_repo
